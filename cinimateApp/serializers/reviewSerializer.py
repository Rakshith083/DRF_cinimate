from rest_framework import serializers
from cinimateApp.models.reviews import Review

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        exclude=['watchlist','deleted_at'] 
        read_only_fields = ['id']

    #custome serializer field
    watchlistName=serializers.SerializerMethodField()
    def get_watchlistName(self,object):
        return str(object.watchlist.title)
    
    available_on=serializers.SerializerMethodField()
    def get_available_on(self,object):
        return str(object.watchlist.platform.name)
    