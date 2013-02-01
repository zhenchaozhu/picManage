from django.db import models

class Picture(models.Model):
    create_date = models.DateField()
    path = models.CharField(max_length=30)

    class Meta(object):
        app_label = 'picture'
        db_table = 'picture_picture'



