from django.contrib import admin
from test_app.models import Employee, Department


class DepartmentAdmin(admin.ModelAdmin):
    search_fields = ('name', )


class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name', 'department__name')

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)

