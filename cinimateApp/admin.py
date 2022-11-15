from django.contrib import admin
# from cinimateApp.models.movies import Movies
from .models import streamPlatform, watchlist,reviews

# Register your models here.
# admin.site.register(Movies)

admin.site.register(watchlist.WatchList)
admin.site.register(streamPlatform.StreamPlatform)
admin.site.register(reviews.Review)
