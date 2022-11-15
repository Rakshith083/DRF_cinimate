from rest_framework import serializers
from cinimateApp.models.reviews import Review

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        # fields = ["id","header","ratings","description","watchlist","watchlistName","created_at","updated_at",]
        exclude=['is_deleted','watchlist'] 
        read_only_fields = ['id']

    #custome serializer field
    watchlistName=serializers.SerializerMethodField()
    def get_watchlistName(self,object):
        return str(object.watchlist.title)
    