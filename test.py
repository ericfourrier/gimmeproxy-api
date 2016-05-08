#!/usr/bin/env python
# -*- coding: utf-8 -*-u

"""
Purpose : Some tests for the class GimmeProxyApi

To run the tests : $ python -m unittest -v test
"""

import unittest
from gpapi.getproxies import GimmeProxyApi
from gpapi.exceptions import InvalidParameters


class TestGimmeProxyApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ creating test data set for the test module """
        cls.api = GimmeProxyApi()

    def test_check_params(self):
        self.assertRaises(InvalidParameters, self.api._check_params, {'supportsHttp': True})
        self.assertRaises(InvalidParameters, self.api._check_params, {'api_key': 'dfdfd'})

    def test_get_proxy(self):
        params = self.api.custom_params
        proxy = self.api.get_proxy(**params)
        self.assertIsInstance(proxy, dict)
        for k in self.api.response_parameters:
            self.assertIn(k, proxy.keys())
        for k, v in params.items():
            if k != 'maxCheckPeriod':
                self.assertEqual(proxy[k], v)
