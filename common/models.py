from django.db import models

#Blue Print for model
#모든 applications에서 공유되는 코드를 가지고 있다. 
class CommonModel(models.Model):
    """Common Model Definition"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #DB에 추가하지 않을 model
    #Django에서 Model을 configure할 때 사용
    class Meta:
        abstract = True #reuse this code
        

