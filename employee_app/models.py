from django.db import models


class Branch(models.Model):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'

    def __str__(self):
        return f'{self.title} - {self.address}'


class Department(models.Model):
    title = models.CharField(max_length=100)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self):
        return f'{self.title} - {self.branch.title}'


class Position(models.Model):
    title = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return f'{self.title} - {self.department.title}'


class Employee(models.Model):
    fullname = models.CharField(max_length=100, help_text='ФИО')
    birth_date = models.DateField()
    salary = models.DecimalField(max_digits=15, decimal_places=2, help_text='Зарплата')
    receipt_date = models.DateField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE, help_text='Должность')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return (f'{self.fullname} - {self.position.title} - {self.position.department.title} - '
                f'{self.position.department.branch.title}')
