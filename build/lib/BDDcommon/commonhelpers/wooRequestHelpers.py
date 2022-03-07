from woocommerce import API
from BDDcommon.commonhelpers.credentialsHelper import CredentialsHelper
import logging as logger


class WooRequestsHelper(object):

    def __init__(self):

        creds_helper = CredentialsHelper()
        wc_reds = creds_helper.get_wc_api_keys()

        self.wcapi = API(
            url="http://example.com",
            consumer_key=wc_reds['wc_key'],
            consumer_secret=wc_reds['wc_secret'],
            version="wc/v3"
        )

    def assert_status_code(self):
        assert self.rs.status_code == self.expected_status_code, "Bad status code. Endpoint: {}, Params: {}. " \
            "Actual status code: {}, Expected status code: {}, Response body: {}"\
            .format(self.wc_endpoint, self.params, self.rs.status_code, self.expected_status_code,self.rs.json())

    def get(self, wc_endpoint, params=None, expected_status_code=200):

        self.rs = self.wcapi.get(wc_endpoint, params=params)
        self.wc_endpoint = wc_endpoint
        self.expected_status_code = expected_status_code
        self.params = params
        self.assert_status_code()

    def post(self, wc_endpoint, params=None, expected_status_code=200):
        logger.info(f"Params: {params}")
        self.rs = self.wcapi.post(wc_endpoint, data=params)
        self.wc_endpoint = wc_endpoint
        self.expected_status_code = expected_status_code
        self.params = params
        self.assert_status_code()

        return self.rs.json()

    def delete(self, wc_endpoint, params=None, expected_status_code=200):
        self.rs = self.wcapi.delete(wc_endpoint, params=params)
        self.wc_endpoint = wc_endpoint
        self.expected_status_code = expected_status_code
        self.params = params
        self.assert_status_code()

        return self.rs.json()
        pass

    def put(self):
        pass
