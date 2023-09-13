from django.urls import path

from . import views


urlpatterns = [
    path('branch/', views.BranchListAPIView.as_view()),
    path('branch/create/', views.BranchCreateAPIView.as_view()),
    path('branch/<int:pk>/', views.BranchRetrieveAPIView.as_view()),
    path('branch/<int:pk>/delete/', views.BranchDestroyAPIView.as_view()),
    path('branch/<int:pk>/update/', views.BranchUpdateAPIView.as_view()),

    path('department/', views.DepartmentListAPIView.as_view()),
    path('department/create/', views.DepartmentCreateAPIView.as_view()),
    path('department/<int:pk>/', views.DepartmentRetrieveAPIView.as_view()),
    path('department/<int:pk>/delete/', views.DepartmentDestroyAPIView.as_view()),
    path('department/<int:pk>/update/', views.DepartmentUpdateAPIView.as_view()),

    path('position/', views.PositionListAPIView.as_view()),
    path('position/create/', views.PositionCreateAPIView.as_view()),
    path('position/<int:pk>/', views.PositionRetrieveAPIView.as_view()),
    path('position/<int:pk>/delete/', views.PositionDestroyAPIView.as_view()),
    path('position/<int:pk>/update/', views.PositionUpdateAPIView.as_view()),

    path('employee/', views.EmployeeListAPIView.as_view()),
    path('employee/create/', views.EmployeeCreateAPIView.as_view()),
    path('employee/<int:pk>/', views.EmployeeRetrieveAPIView.as_view()),
    path('employee/<int:pk>/delete/', views.EmployeeDestroyAPIView.as_view()),
    path('employee/<int:pk>/update/', views.EmployeeUpdateAPIView.as_view()),

    path('branch/<str:branch_name>/department/<str:department_name>/employees/',
         views.BranchDepartmentEmployeesAPIView.as_view()),
]
