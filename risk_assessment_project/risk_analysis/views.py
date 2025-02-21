from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.http import JsonResponse    
from .models import Risk_Assessment
from .serializers import RiskSerializer
from django.views.decorators.csrf import csrf_exempt
import json
import numpy as np
import joblib
import os

def home(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def reports(request):
    return render(request, 'reports.html')

def settings(request):
    return render(request, 'settings.html')


@csrf_exempt  # Allow AJAX requests
def update_settings(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # Get JSON data
            username = data.get("username", "")
            email = data.get("email", "")
            theme = data.get("theme", "light")

            if not username or not email:
                return JsonResponse({"success": False, "error": "Fields cannot be empty!"}, status=400)

            # Save the updated settings (For now, just returning them)
            return JsonResponse({"success": True, "username": username, "email": email})

        except json.JSONDecodeError:
            return JsonResponse({"success": False, "error": "Invalid JSON data!"}, status=400)

    return JsonResponse({"success": False, "error": "Invalid request method!"}, status=405)


def add_business_page(request):
    return render(request, 'add_business.html') 


@api_view(['POST', 'PUT', 'DELETE', 'PATCH', 'GET'])
def add_business(request):
    print("Received Data:", request.data)  

    if request.method == 'POST':
        serializer = RiskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("✅ Data saved successfully!")  # Debugging line
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("❌ Errors:", serializer.errors)  # Debugging line
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def dashboard(request):
    return render(request, 'dashboard.html')

def get_business_data(request):
    businesses = list(Risk_Assessment.objects.values())
    return JsonResponse({"businesses": businesses})


# Create Business Risk Entry (POST) & Get All Entries (GET)
@api_view(['GET', 'POST'])
def business_risk_list(request):
    if request.method == 'GET':
        risks = Risk_Assessment.objects.all()
        serializer = RiskSerializer(risks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RiskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Get, Update, Delete a Single Business Risk Entry
@api_view(['GET', 'PUT', 'DELETE'])
def business_risk_detail(request, pk):
    try:
        business = Risk_Assessment.objects.get(pk=pk)
    except Risk_Assessment.DoesNotExist:
        return Response({"error": "Business risk entry not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RiskSerializer(business)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RiskSerializer(business, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        business.delete()
        return Response({"message": "Business risk entry deleted."}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def assess_risk(request, pk):
    try:
        business = Risk_Assessment.objects.get(pk=pk)
    except Risk_Assessment.DoesNotExist:
        return JsonResponse({"error": "Business not found"}, status=404)

    model_path = os.path.join(os.path.dirname(__file__), 'risk_model.pkl')
    if not os.path.exists(model_path):
        return JsonResponse({"error": "Model not found"}, status=500)

    model = joblib.load(model_path)
    features = np.array([[business.financial_stability, business.market_risk, 
                          business.operational_risk, business.compliance_risk,
                          business.cybersecurity_risk, business.supply_chain_risk,
                          business.reputation_risk]])

    risk_score = model.predict(features)[0]
    business.risk_score = risk_score
    business.save()

    return JsonResponse({"business_name": business.business_name, "risk_score": risk_score})

