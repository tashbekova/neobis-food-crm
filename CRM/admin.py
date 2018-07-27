from django.contrib import admin
from CRM.models import *
# Register your models here.
admin.site.register([Category,Check,ServicePercentage])
admin.site.register(Department)
admin.site.register(Meal)
admin.site.register(MealsToOrder)
admin.site.register(Role)
admin.site.register(User)
admin.site.register(Status)
admin.site.register(Table)

class MealInline(admin.StackedInline):
    model = MealsToOrder
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    inlines = [MealInline, ]

admin.site.register(Order, OrderAdmin)
