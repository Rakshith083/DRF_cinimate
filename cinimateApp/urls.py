"""cinimate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
# from cinimateApp import views as movieViews
from .views.streamPlatformViews import StreeaPlatformListAV,StreamPlatformAV,StreamPlatformVS
from .views.watchlistViews import WatchlistAV,WatchlistDetailsAV
from .views.reviewViews import ReviewList,ReviewDetails,ReviewCreate
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'/streams', StreamPlatformVS,basename='straemPlatform')

urlpatterns = [
    # path('/',movieViews.MovieList.as_view()),
    # path('/<int:id>',movieViews.MovieDetailsAV.as_view()),
    path ('/watchlists',WatchlistAV.as_view(), name='watchlist-list'),
    path ('/watchlists/<int:id>',WatchlistDetailsAV.as_view(),name='watchlist-detail'),
    path ('/watchlists/<int:id>/reviews',ReviewList.as_view(),name='watchlist-review'),
    path ('/watchlists/<int:id>/reviews-create',ReviewCreate.as_view(),name='watchlist-review-create'),
    # path ('/streams',StreeaPlatformListAV.as_view()),
    # path ('/streams/<int:id>',StreamPlatformAV.as_view()),
    path('',include(router.urls)),
    path('/reviews/<int:pk>',ReviewDetails.as_view(),name='review-details'),
]
