from datetime import date, timedelta

from rest_framework import serializers

from .models import Branch, Department, Position, Employee


class BranchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branch
        fields = ['id', 'title', 'address']


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ['id', 'title', 'branch']


class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = ['id', 'title', 'department']


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ['id', 'fullname', 'birth_date', 'salary', 'receipt_date', 'position']

    def validate_birth_date(self, value):
        birth_day = date.today() - timedelta(days=365 * 25)
        if not value <= birth_day:
            raise serializers.ValidationError('Возраст не может быть младше 25 лет')
        return value

    def validate_receipt_date(self, value):
        min_date = date.today() + timedelta(days=1)
        if not value <= min_date:
            raise serializers.ValidationError('Дата начала работы не может быть раньше завтрашнего дня')
        return value

