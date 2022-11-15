from rest_framework import serializers
from cinimateApp.models.reviews import Review

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ["id","header","description","active","created_at","updated_at",]
        # exclude=['is_deleted',] 
        read_only_fields = ['id']