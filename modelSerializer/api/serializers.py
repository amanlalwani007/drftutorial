from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['name','roll','city']
    # To add validators and constraint  to a field  Model
    # name=serializers.CharField(read_only=True)
    # or
    # read_only_fields=['name','roll']
