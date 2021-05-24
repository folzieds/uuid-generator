from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

import datetime, uuid
from .serialiser import UUIDSerializer
from .models import UUID

# Create your views here.
@api_view(['GET'])
def gen_uuid(request):
    new_random_uuid = UUID(timestamp=str(datetime.datetime.now()), uuid=str(uuid.uuid4()))
    new_random_uuid.save()

    uuids = UUID.objects.all().filter().order_by('-id')
    uuids_dict = {}
    
    for i in uuids:
        uuids_dict.update({i.timestamp:i.uuid})

    return Response(uuids_dict)