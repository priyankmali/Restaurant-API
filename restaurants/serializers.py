from rest_framework import serializers
from restaurants.models import*

# Restaurant
class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

# MenuItem
class MenuItemSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer(read_only=True)
    restaurant_id = serializers.PrimaryKeyRelatedField(queryset=Restaurant.objects.all(),source='restaurant', write_only=True)

    #by using name through
    # restaurant_name = serializers.SlugRelatedField(queryset=Restaurant.objects.all(), slug_field='name',source='restaurant',write_only=True)

    class Meta:
        model=MenuItem
        fields='__all__'

# RestaurantLike
class RestaurantLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model=RestaurantLike
        fields = '__all__'

# MenuItemLike
class MenuItemLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model=MenuItemLike
        fields='__all__'

#MenuItemSave
class MenuItemSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model=MenuItemSave
        fields='__all__'

