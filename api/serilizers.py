from rest_framework import serializers

from api.models import Company, Employee

# Create Serilaizers here.
class CompanySerliaizer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()
    class Meta:
        model = Company
        fields= '__all__'


class EmployeeSerliaizer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields= '__all__'