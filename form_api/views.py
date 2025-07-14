from django.shortcuts import render
# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import (
    wheelSpecsFormSerializer,
    WheelSpecsFormCreateSerializer
)

class WheelSpecsFormCreateView(APIView):
    def post(self, request):
        serializer = WheelSpecsFormCreateSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            return Response({
                "success": True,
                "message": "Wheel specification submitted successfully.",
                "data": {
                    "formNumber": instance.form_number,
                    "submittedBy": instance.submitted_by,
                    "submittedDate": instance.submitted_date,
                    "status": instance.status
                }
            }, status=status.HTTP_201_CREATED)
        return Response({"success": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class WheelSpecsFormListView(APIView):
    def get(self, request):
        form_number = request.GET.get("formNumber")
        submitted_by = request.GET.get("submittedBy")
        submitted_date = request.GET.get("submittedDate")

        filters = {}
        if form_number:
            filters["form_number"] = form_number
        if submitted_by:
            filters["submitted_by"] = submitted_by
        if submitted_date:
            filters["submitted_date"] = submitted_date

        queryset = wheelSpecsForm.objects.filter(**filters)
        serializer = wheelSpecsFormSerializer(queryset, many=True)
        return Response({
            "success": True,
            "message": "Filtered wheel specification forms fetched successfully.",
            "data": serializer.data
        })


