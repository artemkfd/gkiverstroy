from ninja import NinjaAPI
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Client 
from .schema import ClientIn, ClientOut
from typing import List

api = NinjaAPI()

@api.post("/clients", response=ClientOut)
def create_client(request, data: ClientIn):
    client = Client.objects.create(**data.dict())
    return ClientOut.from_orm(client) 


@api.get("/clients", response=List[ClientOut])
def get_clients(request):
    clients = Client.objects.all()
    return [ClientOut.from_orm(client) for client in clients]

@api.get("/clients/{client_id}", response=ClientOut)
def get_client(request, client_id: int):
    client = get_object_or_404(Client, id=client_id)
    return ClientOut.from_orm(client)