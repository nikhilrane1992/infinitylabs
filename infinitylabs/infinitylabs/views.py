from django.http import JsonResponse
from django.shortcuts import render_to_response
from models import *
from django.core.exceptions import ObjectDoesNotExist
import json
from django.contrib.auth import authenticate, login
import jwt
from decorators import is_token_valid
SECRET = "yyJOHrqYiXTNrPS2OHMJuEtyy474duSs"


def index(request):
    return render_to_response('index.html')


def login_view(request):
    return render_to_response('login.html')


def auth_view(request):
    params = json.loads(request.body)
    username = params['username']
    password = params['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return JsonResponse({
            "validation": "Login Successful",
            "status": True,
            "token": jwt.encode({'username': username}, SECRET, algorithm='HS256')
        })
    else:
        return JsonResponse({
            "validation": "Authentication failure",
            "status": False
        })


@is_token_valid
def save_router_details(request):
    params = json.loads(request.body)
    loopback = params.pop('loopback')
    router, created = RouterDetails.objects.update_or_create(
        loopback=loopback, defaults=params
    )
    return JsonResponse({
        "validation": "Saved Successfully",
        "status": True
    })


@is_token_valid
def router_details(request):
    params = json.loads(request.body)
    kwargs = {}
    if params.get('loopback'):
        kwargs['loopback'] = params.get('loopback')
    if params.get('router_type'):
        kwargs['router_type'] = params.get('router_type')
    return JsonResponse({
        "data": [{
            "loopback": router.loopback,
            "hostname": router.hostname,
            "brand": router.brand,
            "sap_id": router.sap_id,
            "mac_address": router.mac_address,
            "model_number": router.model_number,
            "router_type": router.router_type,
            "id": router.id
        } for router in RouterDetails.objects.filter(**kwargs)],
        "status": True,
    })


@is_token_valid
def delete_router_details(request):
    params = json.loads(request.body)
    loopback = params.pop('loopback')
    RouterDetails.objects.get(loopback=loopback).delete()
    return JsonResponse({
        "validation": "Deleted Successfully",
        "status": True
    })
