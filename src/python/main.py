import requests
import json

from io import BytesIO

from cryptio.cryptio import Cryptio

def main():
	cryptio = Cryptio()
	cryptio.enumerate_and_print_value_of_portfolio()

##### CALL MAIN METHOD #####
main()