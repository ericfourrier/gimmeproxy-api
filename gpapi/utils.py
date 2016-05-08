import time


def convert_proxy_to_requests(proxy):
    """
    This function convert a string ip:port to the requests package proxy format

    """
    return {'http': 'http://{}'.format(proxy), 'https': 'http://{}'.format(proxy)}


def convert_proxy_to_string(proxy):
    """ This function convert a requests proxy format to a string format """
    return proxy['http'].split('//')[1]


class Proxy(object):
    """
    This is a class for a proxy object

    Arguments
    ---------
    - proxy : dictionnary gathering all infos about a proxy like ip, port, last_update, scraped_at
    - _last_time_used : time, time of the last utilization of the proxies
    - _nb_calls : the number of times the proxy was called
    - _nb_failures : the number of time the proxy failed
    - _nb_sucess : the number of sucess from the calls
    - _test_passed : if the test from ProxyChecker is passed

    Return
    -------
    a Proxy class with all infos as instance variables
    """

    def __init__(self, proxy_dict):
        # set attribute from the proxy dict
        self.proxy_dict = proxy_dict
        for k, v in proxy_dict.items():
            setattr(self, k, v)
        self._last_time_used = None
        self._nb_calls = 0
        self._nb_failures = 0
        self._nb_sucess = 0
        self._test_passed = None

    def __repr__(self):
        return """<Proxy(ip_address={0}, port={1}, ...)>""".format(self.ip_address, self.port)

    def use_proxy(self):
        """ Update _last_time_used to compute the nb seconds since last call to the proxy """
        self._nb_calls += 1
        self._last_time_used = time.time()

    def get_last_time_used(self):
        """ Return _last_time_used into a datetime format """
        return time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime(self._last_time_used))

    def used_since(self):
        """ Return the nb seconds since the proxy aws used """
        return time.time() - self._last_time_used

    def has_failed(self):
        self.nb_failures += 1

    def has_suceed(self):
        self.nb_sucess += 1

    def to_dict(self):
        return {'_last_time_used': self._last_time_used,
                '_nb_calls': self._nb_calls,
                '_nb_failures': self._nb_failures,
                '_nb_sucess': self._nb_sucess,
                '_test_passed': self._test_passed,
                'anonymity_level': self.anonymity_level,
                'connection_time': self.connection_time,
                'country': self.country,
                'ip_address': self.ip_address,
                'last_update': self.last_update,
                'last_update_raw': self.last_update_raw,
                'number_dead_time': self.number_dead_time,
                'number_live_time': self.number_live_time,
                'port': self.port,
                'requests_proxy': self.requests_proxy}
