from rest_framework import serializers
from CRM.models import *
class CategorySerializer(serializers.ModelSerializer):
    serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('name','department')

class TableSerializer(serializers.ModelSerializer):
    serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Table
        fields = ['name']

class StatusSerializer(serializers.ModelSerializer): 
    serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Status
        fields = ['name']

class ServicePercentageSerializer(serializers.ModelSerializer):
    serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = ServicePercentage
        fields = ['percentage']

class RoleSerializer(serializers.ModelSerializer): 
    serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Role
        fields = ['name']

class DepartmentSerializer(serializers.ModelSerializer):
    serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Department
        fields = ('__all__')


class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField()
 
    class Meta(object):
        model = User
        fields = ('id','name','surname','email','password',
                  'phone','date_joined' )
        extra_kwargs = {'password': {'write_only': True}}

class MealSerializer(serializers.ModelSerializer):
    serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Meal
        fields = ('name', 'price', 'description','category')

class MealsToOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealsToOrder
        fields = ('__all__')

class OrderSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)
    tables = TableSerializer(many=True)
    meals = MealSerializer(many=True)

    class Meta:
        model = Order
        fields = ('users','tables','is_it_open','date','meals')

    def create(self, validated_data):
        users = validated_data.pop('users')
        tables = validated_data.pop('tables')
        meals = validated_data.pop('meals')
        
        order=Order.objects.create(**validated_data)

        for user in users:
            User.objects.create(order=order, **user)
        for table in tables:
            Table.objects.create(order=order,**table)
        for meal in meals:
            Meal.objects.create(order=order,**meal)
            
        return order

class CheckSerializer(serializers.ModelSerializer):
    orders =OrderSerializer(many=True)
    percentages = ServicePercentageSerializer(many=True)

    class Meta:
        model = Order
        fields = ('orders','date','percentages')
    
    def create(self, validated_data):
        orders = validated_data.pop('orders')
        percentages = validated_data.pop('percentages')
        
        check=Check.objects.create(**validated_data)

        for order in orders:
            Order.objects.create(check=check, **role)
        for percentage in percentages:
            ServicePercentage.objects.create(check=check,**table)
            
        return check
    