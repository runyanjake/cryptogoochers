## cryptogoochers
Crypto stock trader to teach me about quantitative finance &amp; GCP/AWS microservices.

# Install Steps

Create python env with venv:
	virtualenv --python=/usr/bin/python3 cryptotrader #makes 'cryptotrader' folder with our env.
	mv cryptotrader/ env #so the activate command is easier

Enable new env:
	source env/bin/activate #activate turns it on

Setup what we need for this project in python env:
	Python requirements
		sudo apt install libcurl4-openssl-dev libssl-dev
		sudo apt-get install python-dev
		sudo apt-get install python3-dev
	Requests
		pip3 install requests

AWS database connection
	make sure local mysql is running, you need to have a virtual socket thing open (/var/run/mysqld/mysqld.sock).
	It's created when you turn on mysql with sudo service mysql start. (also, sudo service mysql status.)

# Other

Using Nomics for free crypto api
	http://docs.nomics.com/

Created using Python 3.6.9
	https://www.python.org/downloads/release/python-369/

Curl syntax reference:
	https://curl.trillworks.com/