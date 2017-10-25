from django.http import JsonResponse
from django.shortcuts import render_to_response
from models import *
from django.core.exceptions import ObjectDoesNotExist
import jwt
SECRET = "yyJOHrqYiXTNrPS2OHMJuEtyy474duSs"


def check_athentication(encoded):
    try:
        jwt.decode(encoded, SECRET, algorithms=['HS512', 'HS256'])
        return True
    except DecodeError:
        return False


def auth_view(request):
    params = json.loads(request.body)
    username = params['username']
    password = params['password']
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        request.META['Token'] = jwt.encode(SECRET, algorithm='HS256')
        return JsonResponse({
            "validation": "Login Successful",
            "status": True
        })
    else:
        return JsonResponse({
            "validation": "Authentication failure",
            "status": False
        })


def router_details(request):
    if not check_athentication(request.META['Token']):
        return JsonResponse({
            "status": False,
            "validation": "Invalid Token"
        })
    return JsonResponse({
        "data": [{
            "loopback": router.loopback,
            "hostname": router.hostname,
            "brand": router.brand,
            "item_height": router.item_height,
            "item_weight": router.item_weight,
            "dimensions": router.dimensions,
            "model_number": router.model_number,
            "id": router.id
        } for router in RouterDetails.objects.all()],
        "status": True,
    })
