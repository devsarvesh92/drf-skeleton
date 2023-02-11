from base.models import Item
from rest_framework import serializers

class ItemSerizalier(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"
