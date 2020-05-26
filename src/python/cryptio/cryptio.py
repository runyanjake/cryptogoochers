import json 
import requests

class Cryptio: 

	def __init__(self):
		pass

	def portfolio_file_to_dict(self):
		f = open("resource/holdings.txt", 'r', encoding="utf-8")
		js = json.loads(f.read())
		portfolio = js['portfolio']
		return portfolio

	def enumerate_and_print_value_of_portfolio(self):
		#1. get portfolio
		portfolio = self.portfolio_file_to_dict()
		ids = ""
		holdings = {}
		for t in portfolio:
			ids = ids + t + ","
			holdings[t] = portfolio.get(t)
		ids = ids[:-1]
		#2. get prices
		c = open("resource/credentials.txt")
		credentials = json.load(c)
		nomics_api_key = credentials.get("api_key")
		params = (
			('key', nomics_api_key),
			('ids', ids),
			('interval', "1d"),
			('convert', "USD"))
		response = requests.get('https://api.nomics.com/v1/currencies/ticker', params=params)
		prices = response.json()
		# #3. compute portfolio value
		portfolio_total = 0
		for result in prices:
			result_ticker = result['id']
			current_price = float(result['price'])
			holding_amt = holdings[result_ticker]
			portfolio_total = portfolio_total + (holding_amt * current_price)
			print("" + str(holding_amt) + " of " + str(result_ticker) + " at " + str(current_price) + ".")
		#4. print
		print("Total potrfolio value: " + str(portfolio_total))