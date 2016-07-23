#!/usr/bin/env python
# -*- coding: utf-8 -*-u

"""
author = efourrier

Purpose : this is a small python wrapper for the http://gimmeproxy.com/api/
"""



# Import Packages and helpers

import os
import json
import pickle
import requests

from .exceptions import InvalidParameters, TooManyRequests

# Main Class

class GimmeProxyApi(object):
    """ This is a class to get proxies via the gimmeproxy api and process them
    in order to get the right format for the proxies parameter of the requests package """
    _nb_calls_per_min_limit = 60
    nb_total_calls = 0
    parameters_name = ["apikey", "get", "post", "cookies", "referer", "user-agent",
                       "supportsHttps", "anonymityLevel", "protocol", "port", "country", "maxCheckPeriod"]
    parameters_value = ["string", "true/false", "true/false", "true/false", "true/false",
                        "true/false", "0/1", "http/socks4/socks5", "integer", "string", "integer, seconds"]
    parameters_description = ["API key, if you have one, allows to scrape faster", "GET requests support", "POST requests support",
                              "Cookies support", "referer header support", "user-agent header support",
                              "HTTPS support", "Anonymity level, 1 - anonymous, 0 - not anonymous",
                              "Proxy protocol", "Proxy port", "Return only proxies with specified country",
                              "Return only proxies checked in last maxCheckPeriod seconds"]
    response_parameters = ['ipPort', 'cookies', 'tsChecked', 'protocol',
                           'curl', 'get', 'ip', 'supportsHttps', 'websites', 'user-agent',
                           'type', 'referer', 'country', 'post',
                           'otherProtocols', 'anonymityLevel', 'port']

    def __init__(self, apikey=None):
        self.apikey = apikey
        if self.apikey is None:
            print("You have no api key you are limited to {} calls per minute".format(
                self._nb_calls_per_min_limit))
        self.base_url = "http://gimmeproxy.com/api/getProxy"
        self.custom_params = {'get': True, 'supportsHttps': True, 'anonymityLevel': 1,
                              'maxCheckPeriod': 600, 'supportsHttps': True, 'user-agent': True,
                              'protocol': 'http'}

    def get_infos_parameters(self):
        """ Returns a dict infos with as key parameter and values a dict with values and description """
        zip_params = zip(self.parameters_name,
                         self.parameters_value, self.parameters_description)
        infos_params = {}
        for (n, v, d) in zip_params:
            infos_params[n] = {'value': v, "description": d}
        return infos_params

    def _check_params(self, params):
        """ Check that a dict of parameters are valid for the api """
        params_names = params.keys()
        for k in params_names:
            if k not in self.parameters_name:
                raise InvalidParameters(
                    "Additionnal parameters should be in {}".format(self.parameters_name))

    def get_proxy(self, **kwargs):
        """
        Get a random proxy from the http://gimmeproxy.com/api/

        Arguments
        ---------
        **kwargs : to add additionnal parameters to request example :
        g = GimmeProxyApi()
        g.get_proxies(country="US")
        g.get_proxies(**g.custom_params)

        Returns
        -------
        raw json response from the api

        """
        self._check_params(kwargs)
        r = requests.get(self.base_url, params=kwargs)
        if r.status_code == 200:
            json_response = r.json()
        elif r.status_code == 429:
            raise TooManyRequests("You did more than 60 requests in 60 seconds, slow down !")
        else:
            raise Exception("An unknown error occured, status_code = {}".format(r.status_code))
        self.nb_total_calls += 1
        return json_response

    def reset(self):
        """ Reset nb_total_calls """
        self.nb_total_calls = 0
