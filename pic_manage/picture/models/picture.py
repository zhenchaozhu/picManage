from django.db import models

class Picture(models.Model):
    create_date = models.DateTimeField()
    path = models.CharField(max_length=1000)

    @staticmethod
    def get_path(page_num):
        start = page_num * 10
        end = start + 10
        return [obj.path for obj in Picture.objects.all()[start: end]]

    class Meta(object):
        app_label = 'picture'
        db_table = 'picture_picture'





