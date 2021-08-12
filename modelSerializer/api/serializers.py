from rest_framework import serializers
from .models import Student

def starts_with_r(value):
    if value[0].lower()!='r':
        raise serializers.ValidationError('Name should be start with R')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['name','roll','city']
    # To add validators and constraint  to a field  Model
    # name=serializers.CharField(read_only=True)
    # or
    # read_only_fields=['name','roll']
    # or
    # extra_kwargs = {'name':{'read_only':True}}
    def validate_roll(self,value):
        if value>=200:
            raise serializers.ValidationError("Seat Full")
        return value
