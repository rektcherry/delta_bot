import alpaca_trade_api as tradeapi
import os
from dotenv import load_dotenv
load_dotenv()
# environment variables
api_key = os.getenv("api_key")
secret_key = os.getenv("secret_key") 
url = os.getenv("url")

class strategy(object):
    def __init__(self):
        global api_key
        global secret_key
        global url
        self.key = api_key
        self.secret = secret_key
        self.address = url
        self.api = api = tradeapi.REST(self.key, self.secret, self.address)
        self.symbol = 'BTCUSD'
        self.current_order = None # when not NONE, position is open
        self.last_price = 1
        try: 
            self.position = int(self.api.get_position(self.symbol).qty) # get current position
        except:
            self.position = 0 # if this gets triggered, no position exists

    def submit_order(self,target):
        if self.current_order is not None:
            self.api.cancel_order(self.current_order.id) # this cancels the possible second order
        delta = target - self.position
        if delta == 0:
            return
        print(f'processing the order for {target} shares')
        if delta > 0:
            buy_quantity = delta
            if self.position < 0:
                buy_quantity = min(abs(self.position), buy_quantity)
            print(f'buying {buy_quantity} shares') 
            self.current_order = self.api.submit_order(self.symbol, buy_quantity, 'buy', 'limit', 'day',self.last_price)
        elif delta < 0:
            sell_quantity = abs(delta)
            if self.position > 0:
                sell_quantity = min(abs(self.position),sell_quantity)
            print(f'selling {sell_quantity} shares') 
            self.current_order = self.api.submit_order(self.symbol, sell_quantity, 'sell', 'limit', 'day',self.last_price)
if __name__ == '__main__' :
    s = strategy()
    s.submit_order(1)