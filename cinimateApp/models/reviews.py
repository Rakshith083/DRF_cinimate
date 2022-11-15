from django.db import models
from cinimateApp.models.comman.baseModel import BaseModel
from cinimateApp.models.comman.softdelete import SoftDeleteModel
from cinimateApp.models.watchlist import WatchList
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Review(BaseModel,SoftDeleteModel):
    header=models.CharField(max_length=50)
    description =models.CharField(max_length=250,null=True)
    ratings=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    # active=models.BooleanField(default=True)
    watchlist=models.ForeignKey(WatchList,on_delete=models.CASCADE,related_name='reviews')

    def __str__(self):
        return self.header+" : "+str(self.ratings)