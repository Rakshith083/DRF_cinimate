from cinimateApp.models.reviews import Review
from cinimateApp.serializers.reviewSerializer import ReviewSerializer
from cinimateApp.models.watchlist import WatchList
from rest_framework.mixins import (ListModelMixin,CreateModelMixin,
                                    RetrieveModelMixin,UpdateModelMixin,
                                    DestroyModelMixin)
from rest_framework.generics import (GenericAPIView,CreateAPIView,
                                    ListAPIView,ListCreateAPIView,
                                    RetrieveUpdateDestroyAPIView)
# class ReviewList(ListModelMixin,CreateModelMixin,GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class ReviewDetails(UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin,GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

class ReviewList(ListAPIView):
    # queryset = Review.objects.filter()
    serializer_class = ReviewSerializer
    def get_queryset(self):
        watchlistId = self.kwargs['id']
        return Review.objects.filter(watchlist=watchlistId)

class ReviewDetails(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.filter()
    serializer_class = ReviewSerializer

class ReviewCreate(CreateAPIView):
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        watchlistId = self.kwargs.get('id')
        movie=WatchList.objects.get(id=watchlistId)
        serializer.save(watchlist=movie)

