from django.db import models
from cinimateApp.models.comman.baseModel import BaseModel
from cinimateApp.models.comman.softdelete import SoftDeleteModel
from softdelete.models import SoftDeleteObject

class StreamPlatform(BaseModel,SoftDeleteObject):
    name=models.CharField(max_length=30)
    about=models.CharField(max_length=150)
    website=models.URLField(max_length=100)
    def __str__(self):
        return self.name