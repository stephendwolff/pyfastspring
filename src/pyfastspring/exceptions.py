
class FastSpringException(Exception):
    """
    Exception raised when the response from the FastSpring API is an error.

    The status, message, and reason attributes are set to the values returned by
    the API.
    """

    def __init__(self, error_msg, api_status, api_message, api_reason):
        self.status, self.message, self.reason = api_status, api_message, api_reason
        super(FastSpringException, self).__init__(error_msg)
