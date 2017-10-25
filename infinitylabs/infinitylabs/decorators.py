import jwt
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth import logout
SECRET = "yyJOHrqYiXTNrPS2OHMJuEtyy474duSs"


def is_token_valid(function):
    def wrap(request, *args, **kwargs):
        try:
            jwt.decode(request.META.get('HTTP_AUTHORIZATION'), SECRET, algorithms=['HS512', 'HS256'])
            return function(request, *args, **kwargs)
        except jwt.DecodeError:
            logout(request)
            return JsonResponse({
                "status": False,
                "validation": "Invalid Token",
                "redirect_url": "/"
            })
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
