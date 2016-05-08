#!/usr/bin/env python
# -*- coding: utf-8 -*-u

"""
author = efourrier

Purpose : Exceptions for the GimmeProxyApi
"""

class InvalidParameters(Exception):
    """ Invalid parameters Exception """
    pass

class TooManyRequests(Exception):
    """ Exception when your did more than your twenty requests """
    pass
