# gimmeproxy-api



## Introduction

gpapi is a python wrapper for the GimmeProxy API (http://gimmeproxy.com/#api)

## Installation
Installation via pip is not available now (*coming soon*)

 1. Clone the project on your local computer.

 2. Run the following command

 	* `$ python setup.py install`

## Usage

    from gpapi import GimmeProxyApi
    api = GimmeProxyApi() # initiate the class (you can pass an apikey if you have one)
    random_proxy = api.get_proxy()
    random_proxy_us = api.get_proxy(country="US")
    random_proxy_custom = api.get_proxy(**api.custom_params)
    print("You have called {} times the api".format(api.nb_total_calls))
