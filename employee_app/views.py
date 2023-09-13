from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Branch, Department, Position, Employee
from .serializers import BranchSerializer, DepartmentSerializer, PositionSerializer, EmployeeSerializer


class BranchListAPIView(generics.ListAPIView):
    """
    Вывод всех филлиалов
    """
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class BranchCreateAPIView(generics.CreateAPIView):
    """
    Создание филлиала
    """
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class BranchRetrieveAPIView(generics.RetrieveAPIView):
    """
    Получение информации о филлиале
    """
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class BranchDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление филлиала
    """
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class BranchUpdateAPIView(generics.UpdateAPIView):
    """
    Обновление информации о филлиале
    """
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class DepartmentListAPIView(generics.ListAPIView):
    """
    Вывод всех отделов
    """
    queryset = Department.objects.all().select_related('branch')
    serializer_class = DepartmentSerializer


class DepartmentCreateAPIView(generics.CreateAPIView):
    """
    Создание отдела
    """
    queryset = Department.objects.all().select_related('branch')
    serializer_class = DepartmentSerializer


class DepartmentRetrieveAPIView(generics.RetrieveAPIView):
    """
    Получение информации о отделе
    """
    queryset = Department.objects.all().select_related('branch')
    serializer_class = DepartmentSerializer


class DepartmentDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление отдела
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentUpdateAPIView(generics.UpdateAPIView):
    """
    Обновление информации о отделе
    """
    queryset = Department.objects.all().select_related('branch')
    serializer_class = DepartmentSerializer


class PositionListAPIView(generics.ListAPIView):
    """
    Вывод всех должностей
    """
    queryset = Position.objects.all().select_related('department')
    serializer_class = PositionSerializer


class PositionCreateAPIView(generics.CreateAPIView):
    """
    Создание должности
    """
    queryset = Position.objects.all().select_related('department')
    serializer_class = PositionSerializer


class PositionRetrieveAPIView(generics.RetrieveAPIView):
    """
    Получение информации о должности
    """
    queryset = Position.objects.all().select_related('department')
    serializer_class = PositionSerializer


class PositionDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление должности
    """
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class PositionUpdateAPIView(generics.UpdateAPIView):
    """
    Обновление информации о должности
    """
    queryset = Position.objects.all().select_related('department')
    serializer_class = PositionSerializer


class EmployeeListAPIView(generics.ListAPIView):
    """
    Вывод всех сотрудников
    """
    queryset = Employee.objects.all().select_related('position')
    serializer_class = EmployeeSerializer


class EmployeeCreateAPIView(generics.CreateAPIView):
    """
    Создание сотрудника
    """
    queryset = Employee.objects.all().select_related('position')
    serializer_class = EmployeeSerializer


class EmployeeRetrieveAPIView(generics.RetrieveAPIView):
    """
    Получение информации о сотруднике
    """
    queryset = Employee.objects.all().select_related('position')
    serializer_class = EmployeeSerializer


class EmployeeDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление сотрудника
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeUpdateAPIView(generics.UpdateAPIView):
    """
    Обновление информации о сотруднике
    """
    queryset = Employee.objects.all().select_related('position')
    serializer_class = EmployeeSerializer


class BranchDepartmentEmployeesAPIView(APIView):
    """
    Вывод всех сотрудников данного филиала и отдела
    """
    def get(self, request, branch_name, department_name):
        try:
            branch = Branch.objects.get(title=branch_name)
        except Branch.DoesNotExist:
            return Response({'message': 'Филиал не найден'}, status=status.HTTP_404_NOT_FOUND)

        try:
            department = Department.objects.get(branch=branch, title=department_name)
        except Department.DoesNotExist:
            return Response({'message': 'Отдел не найден'}, status=status.HTTP_404_NOT_FOUND)

        employees = Employee.objects.filter(position__department=department)

        employee_data = {
            'department': department.title,
            'employees': [{'fullname': employee.fullname, 'position': employee.position.title} for employee in
                          employees],
        }

        return Response(employee_data, status=status.HTTP_200_OK)

