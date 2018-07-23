from django.contrib import admin
from CRM.models import *
# Register your models here.
admin.site.register([Category,Check,ServicePercentage])
admin.site.register(Department)
admin.site.register(Meal)
admin.site.register(MealsToOrder)
admin.site.register(Role)
admin.site.register(User)
admin.site.register(Order)
admin.site.register(Status)
admin.site.register(Table)

