"""
A simple module that implements a class for working with the FastSpring orders
and subscription API. Each method corresponds to a documented FastSpring API
endpoint. Data is entered and returned as a dict.
"""

import requests


class FastSpringAPI(object):

    def __init__(self, username, password, api_domain='api.fastspring.com', debug=False):
        """
        Initialize the API object. 'username', and 'password', should
        be available in the integration area of your FastSpring account.
        """
        self.debug = debug
        self.username = username
        self.password = password
        self.api_domain = api_domain

    def get_account_by_id(self, order_id):
        """
        Apply an account ID to return the associated account.
        """
        return self._request('GET', f'accounts/{order_id}')

    def get_account_ids(self, limit=50, page=1):
        """
        Return all account ids (paginated)
        """
        url_path = f"accounts?limit={limit}&page={page}"
        return self._request('GET', url_path)

    def search_accounts_by_parameter(self, parameter, search_value):

        url_path = f"accounts?{parameter}={search_value}"
        return self._request('GET', url_path)

    def get_order_by_id(self, order_id):
        """
        Apply an order ID to return the associated order.

        [FastSpring >>> If you specify multiple order IDs in the request,
        the response will return an array with each order object.]
        """
        return self._request('GET', f'orders/{order_id}')

    def get_orders_by_date_range(self, begin_date, end_date, limit=50, page=1):
        """
        Return all orders within a specific date range

        :param begin_date: datetime (yyyy-mm-dd)
        :param end_date: datetime (yyyy-mm-dd)
        """

        begin_date_str = begin_date.date()
        end_date_str = end_date.date()

        url_path = f"orders?begin={begin_date_str}&end={end_date_str}&limit={limit}&page={page}"
        return self._request('GET', url_path)

    def get_subscription_by_id(self, subscription_id):
        """
        Apply a subscription ID to return the associated subscription.
        """
        return self._request('GET', f'subscriptions/{subscription_id}')

    def get_subscription_entries(self, subscription_id):
        """
        Get all 'order' entries for a subscription, these include 'rebills' which end in a 'b'
        """
        return self._request('GET', f'subscriptions/{subscription_id}/entries')

    def get_subscription_ids(self, limit=50, page=1):
        """
        Return all subscription ids (paginated)
        """

        url_path = f"subscriptions?limit={limit}&page={page}"
        return self._request('GET', url_path)

    def _request(self, method, path, data=None, skip_unparse=False):
        """
        Internal method for making requests to the FastSpring server.
        """
        if path.startswith('/'):
            path = path[1:]

        request_path = f'https://{self.api_domain}/{path}'

        headers = {"Content-type": "application/json"}
        resp = requests.request(
            method,
            request_path,
            auth=(self.username, self.password),
        )
        if self.debug:
            print('-' * 80)
            print('{}'.format(resp.status_code))
            print('{}    {}{}'.format(method, self.api_domain, request_path))
            print(resp.text)
            print('-' * 80)
        resp.raise_for_status()

        return resp.json()
