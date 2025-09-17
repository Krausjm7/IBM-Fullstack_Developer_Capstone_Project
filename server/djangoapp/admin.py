from django.contrib import admin
from .models import CarMake, CarModel


# CarModelInline to show related CarModel instances on the CarMake page
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 3  # Number of extra forms to display


# CarMakeAdmin to customize the admin interface for CarMake
class CarMakeAdmin(admin.ModelAdmin):
    fields = ['name', 'description']
    inlines = [CarModelInline]


# CarModelAdmin to customize the admin interface for CarModel
class CarModelAdmin(admin.ModelAdmin):
    # This list controls which fields are displayed on the change list page.
    list_display = ['name', 'car_make', 'year', 'type']
    # This creates a filter sidebar on the right.
    list_filter = ['car_make', 'type', 'year']
    # This adds a search bar that searches the specified fields.
    search_fields = ['name', 'car_make__name']


# Register models with their custom ModelAdmin classes
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
