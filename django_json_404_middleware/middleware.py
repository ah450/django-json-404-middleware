from django.conf import settings


class JSON404Middleware(object):
    """
    Returns JSON 404 instead of HTML
    """

    def __init__(self, get_response):
        self.get_response = get_response
        self.data_function = settings.JSON404_DATA_FUNCTION

    def __call__(self, request):
        response = self.get_response(request)
        if (
            response.status_code == 404
            and "text/html" in response["content-type"]
        ):
            response = self.data_function(request)
        return response
