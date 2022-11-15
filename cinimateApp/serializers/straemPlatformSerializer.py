from rest_framework import serializers
from cinimateApp.models.streamPlatform import StreamPlatform
from cinimateApp.serializers.WatchlistSerializer import WatchlistSerializer

class StreamPlatformSerializer(serializers.ModelSerializer):
    # watchlist=WatchlistSerializer(many=True, read_only=True) #Get all fieds
    watchlist=serializers.SlugRelatedField(many=True,read_only=True,slug_field='title') #get single required column
    # watchlist=serializers.StringRelatedField(many=True) #get queryset Str string
    # watchlist=serializers.HyperlinkedRelatedField(many=True,lookup_field = 'id',read_only=True,view_name='watchlist-detail')
    
    class Meta:
        model = StreamPlatform
        fields = ['id','name','about','website','created_at','updated_at','watchlist'] 
        # exclude=['is_deleted']
        read_only_fields = ['id']
