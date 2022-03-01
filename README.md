This is a simple delta-based algorithmic trading strategy.
All it does is check if delta is positive to send a buy order and if negative then sell order.
Only one trade can be open at the same time.

I used alpaca platform for api keys. For api information create .env file where you store api keys for privacy: 

.env
1. api_key = 'your api key here'
2. secret_key = 'your secret key here'
3. url = 'url goes here'

Strategy has not been backtested at all, and thus, should not be used with real money. This is a basic code sample to be use as a base for more sophisticated trading robots --