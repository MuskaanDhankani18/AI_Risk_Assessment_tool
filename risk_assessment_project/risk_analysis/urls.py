from django.urls import path
from .views import add_business_page, home, add_business, dashboard, reports, settings, update_settings, get_business_data, assess_risk

urlpatterns = [
    path('', home, name='home'),
    path('add-business/', add_business_page, name='add_business_page'), 
    path('api/add-business/', add_business, name='add_business_api'),
    path('dashboard/', dashboard, name='dashboard'),
    path('reports/', reports, name='reports'),
    path('settings/', settings, name='settings'),
    path('api/update-settings/', update_settings, name='update_settings'),
    path('api/businesses/', get_business_data, name='get_business_data'),
    path('api/assess-risk/<int:pk>/', assess_risk, name='assess_risk'),
]
