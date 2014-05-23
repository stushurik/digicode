from django.core import serializers
from django.http import HttpResponse
from test_app.models import Employee


def get_users(request, key=None):
    employees = \
        Employee.objects.filter(id=key) if key else Employee.objects.all()

    data = serializers.serialize(
        "json",
        employees,
        use_natural_keys=True
    )

    return HttpResponse(
        data,
        mimetype='application/json'
    )
