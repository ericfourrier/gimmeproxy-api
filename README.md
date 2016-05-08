# gimmeproxy-api
[![Travis-CI Build Status](https://travis-ci.org/ericfourrier/gimmeproxy-api.svg?branch=master)](https://travis-ci.org/ericfourrier/ggimmeproxy-api)  ![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)
![Python 3.5](https://img.shields.io/badge/python-3.5-blue.svg)
![License](https://img.shields.io/badge/license-MIT%20License-blue.svg)



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
