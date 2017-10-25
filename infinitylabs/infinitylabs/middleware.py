from django.http import JsonResponse
import jwt
SECRET = "yyJOHrqYiXTNrPS2OHMJuEtyy474duSs"


class AthenticateTokenMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.process_request(request)
        response = self.get_response(request)
        return response

    def process_request(self, request):
        try:
            jwt.decode(request.META['Token'], SECRET, algorithms=['HS512', 'HS256'])
        except jwt.DecodeError:
            return JsonResponse({
                "status": False,
                "validation": "Invalid Token"
            })
