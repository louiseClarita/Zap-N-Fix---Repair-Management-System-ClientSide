from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    email = serializers.EmailField(allow_null=False, default="default@test.com")
    username = serializers.CharField(max_length=150, allow_null=False)
    role = serializers.CharField(max_length=150, allow_null=False, default="Client")
    number = serializers.IntegerField()
    location = serializers.CharField(max_length=150)
    is_active = serializers.BooleanField(default=True)
    is_staff = serializers.BooleanField(default=False)
    is_superuser = serializers.BooleanField(default=False)
    first_name = serializers.CharField(max_length=150, allow_null=False)
    last_name = serializers.CharField(max_length=150, allow_null=False)
    date_joined = serializers.DateTimeField(read_only=True)
    last_login = serializers.DateTimeField(allow_null=True)

    class Meta:
        model = User
        fields = '__all__'


class RepairSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    desc = serializers.CharField()

    status = serializers.CharField(max_length=50)
    repairDate = serializers.DateField(allow_null=True, required=False)
    actualRepairDate = serializers.DateField(allow_null=True, required=False)
    pricing = serializers.DecimalField(max_digits=8, decimal_places=2, allow_null=True, required=False)
    isDelivery = serializers.BooleanField(default=False)
    image = serializers.ImageField(allow_null=True, required=False)
    feedbackRate = serializers.IntegerField(allow_null=True, required=False)
    notes = serializers.CharField(allow_null=True, required=False)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all(), allow_null=True, required=False)
    user_idClient = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), allow_null=True, required=False)
    user_idTech = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), allow_null=True, required=False)

    class Meta:
        model = Repair
        exclude = ('createdDate',)


class BrandSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Brand
        fields = ['desc','type_id']


class TypeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Type
        fields = ['desc']


class ComponentSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Component
        fields = '__all__'


class ProblemSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Problem
        fields = '__all__'