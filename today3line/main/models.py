from django.db import models
from django.utils import timezone

class ParsedData(models.Model):
    url = models.TextField(primary_key=True,)
    title = models.TextField(default = '')
    image_url = models.TextField(default = '/static/default.png')
    line1 = models.TextField(default = '')
    line2 = models.TextField(default = '')
    line3 = models.TextField(default = '')

    def __str__(self): #타이틀로 URL 값이 뜨게 작성함
        return str(self.url)
