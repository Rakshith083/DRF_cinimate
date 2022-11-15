from django.db import models
from cinimateApp.models.comman.baseModel import BaseModel
from cinimateApp.models.comman.softdelete import SoftDeleteModel
from cinimateApp.models.streamPlatform import StreamPlatform
from softdelete.models import SoftDeleteObject
# Create your models here.

class WatchList(BaseModel,SoftDeleteObject):
    title=models.CharField(max_length=250)
    storyline=models.CharField(max_length=250)
    active=models.BooleanField(default=False)
    platform=models.ForeignKey(StreamPlatform,on_delete=models.CASCADE,related_name='watchlist')

    def __str__(self):
        return self.title