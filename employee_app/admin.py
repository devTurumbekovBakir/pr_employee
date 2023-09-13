from django.contrib import admin

from .models import Branch, Department, Position, Employee

admin.site.register(Branch)
admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Employee)
