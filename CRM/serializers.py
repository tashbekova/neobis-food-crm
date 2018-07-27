from rest_framework import serializers
from CRM.models import *


class CategorySerializer(serializers.ModelSerializer):
    serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('name', 'department')


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
    class Meta(object):
        model = User
        fields = ('id', 'name', 'surname', 'email',
                  'phone')
        extra_kwargs = {'password': {'write_only': True}}


class MealSerializer(serializers.ModelSerializer):
    serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Meal
        fields = ('name', 'price', 'description', 'category')


class MealsToOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealsToOrder
        fields = ('__all__')


class OrderSerializer(serializers.ModelSerializer):
    waiters = RoleSerializer()
    tables = TableSerializer()
    meals = MealSerializer(many=True)

    class Meta:
        model = Order
        fields = ('waiters', 'tables', 'date', 'meals')


class CheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Check
        fields = ('date', 'order', 'total_sum')

    def to_representation(self, instance):
        result = super().to_representation(instance)
        order = instance.order
        meal_counts = MealsToOrder.objects.filter(order=order)
        total_sum = 0
        for mc in meal_counts:
            total_sum += (mc.count * mc.meal.price)

        result['total_sum'] = total_sum
        return result
