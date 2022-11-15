#Model Serializer

from rest_framework import serializers
from cinimateApp.models.watchlist import WatchList
from cinimateApp.serializers.reviewSerializer import ReviewSerializer

class WatchlistSerializer(serializers.ModelSerializer):
    # reviews=ReviewSerializer(many=True, read_only=True) #Get all fieds
    # reviews=serializers.HyperlinkedRelatedField(many=True,lookup_field = 'id',read_only=True,view_name='review-detail')
    # reviews=serializers.StringRelatedField(many=True) #get queryset Str string
    # reviews=serializers.SlugRelatedField(many=True,read_only=True,slug_field='ratings') #get single required column

    class Meta:
        model = WatchList
        # fields = ["id","title","storyline","active","platform","platformName","reviews","created_at","updated_at",]
        # fields='__all__'
        exclude=['deleted_at']
        read_only_fields = ['id']

    #custome serializer field
    platformName=serializers.SerializerMethodField()
    def get_platformName(self,object):
        return str(object.platform.name)
