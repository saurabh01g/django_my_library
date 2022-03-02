from django.urls import path

from .views import (EmployeeCreate, EmployeeDelete, EmployeeDetail,
                    EmployeeRetrieve, EmployeeUpdate)

app_name = 'book'  
urlpatterns = [  
    path('emp-gcreate/', EmployeeCreate.as_view(), name='EmployeeCreate'),  
    path('emp-retr/', EmployeeRetrieve.as_view(), name='EmployeeRetrieve'),  
    path('emp-retr/<int:pk>/', EmployeeDetail.as_view(), name='EmployeeDetail'),  
    path('emp-update/<int:pk>/', EmployeeUpdate.as_view(), name='EmployeeUpdate'),  
    path('emp-delete/<int:pk>/', EmployeeDelete.as_view(), name='EmployeeDelete')  

]  
