from rest_framework import serializers
from rest_framework import employees


class employeesSerializer(serializers.ModelSerializer):
    class Meta:
        moedel = employees
        #field = ('first_name', 'last_name')
        fields = '__all__'
