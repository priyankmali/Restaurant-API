from django.contrib import admin
from restaurants.models import*

# Register your models here.

# Resturant
class RestaurantAdmin(admin.ModelAdmin):
    list_display=['name','description','address','contact_number','email','image','opening_time','closing_time','is_active']

admin.site.register(Restaurant,RestaurantAdmin)

#MenuItem
class MenuItemAdmin(admin.ModelAdmin):
    list_display=['menu_name','menu_descripion','price','menu_image','category','is_available']

admin.site.register(MenuItem,MenuItemAdmin)

#RestaurantLike
class RestaurantLikeAdmin(admin.ModelAdmin):
    list_display=[]

admin.site.register(RestaurantLike,RestaurantLikeAdmin)

# MenuItemLike
class MenuItemLikeAdmin(admin.ModelAdmin):
    list_display=[]

admin.site.register(MenuItemLike,MenuItemLikeAdmin)

# MenuItemSave
class MenuItemSaveAdmin(admin.ModelAdmin):
    list_display=[]

admin.site.register(MenuItemSave,MenuItemSaveAdmin)

