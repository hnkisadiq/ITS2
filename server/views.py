# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import status
from server.serializers import FarmSerializer, IdentitySerializer, Property_houseSerializer, Property_farmSerializer, WellSerializer, CropSerializer, HouseSerializer
from server.models import Farm, House, Well, Crop, Property_house, Property_farm, Identity
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view(['GET', 'POST'])
def identity_list(request,format=None):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        temp = Identity.objects.all()
        serializer = IdentitySerializer(temp, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = IdentitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def house_list(request,format=None):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        temp = House.objects.all()
        serializer = HouseSerializer(temp, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = HouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def farm_list(request,format=None):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        temp = Farm.objects.all()
        serializer = FarmSerializer(temp, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FarmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def well_list(request,format=None):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        temp = Well.objects.all()
        serializer = WellSerializer(temp, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = WellSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def crop_list(request,format=None):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        temp = Crop.objects.all()
        serializer = CropSerializer(temp, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CropSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def property_house_list(request,format=None):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        temp = Propert_house.objects.all()
        serializer = Property_houseSerializer(temp, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Property_houseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def property_farm_list(request,format=None):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        temp = Propert_farm.objects.all()
        serializer = Property_farmSerializer(temp, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Property_farmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
