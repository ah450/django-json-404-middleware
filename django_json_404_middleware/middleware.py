from django.conf import settings
from django.http import JsonResponse


def default_response(request):
    data = {"detail": "{0} not found".format(request.path)}
    return JsonResponse(data, content_type="application/json", status=404)


class JSON404Middleware(object):
    """
    Returns JSON 404 instead of HTML
    """

    def __init__(self, get_response):
        self.get_response = get_response
        try:
            self.data_function = settings.JSON404_DATA_FUNCTION
        except AttributeError:
            self.data_function = default_response

    def __call__(self, request):
        response = self.get_response(request)
        if (
            response.status_code == 404
            and "text/html" in response["content-type"]
        ):
            response = self.data_function(request)

        return response
