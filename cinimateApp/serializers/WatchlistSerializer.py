#Model Serializer

from rest_framework import serializers

from cinimateApp.models.watchlist import WatchList
from cinimateApp.serializers.reviewSerializer import ReviewSerializer

class WatchlistSerializer(serializers.ModelSerializer):
    reviews=ReviewSerializer(many=True, read_only=True) #Get all fieds
    class Meta:
        model = WatchList
        fields = ["id","title","storyline","active","platform","platformName","created_at","updated_at",]
        # exclude=['is_deleted',] 
        read_only_fields = ['id']

    #custome serializer field
    platformName=serializers.SerializerMethodField()
    def get_platformName(self,object):
        return str(object.platform)
