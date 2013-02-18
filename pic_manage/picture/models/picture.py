from django.db import models

class Picture(models.Model):
    create_date = models.DateTimeField()
    path = models.CharField(max_length=1000)

    @staticmethod
    def get_path(page_num):
        start = page_num * 8
        end = start + 8
        return [obj.path for obj in Picture.objects.order_by('-id')[start: end]]

    @staticmethod
    def save_img(create_time, path):
        pic = Picture(create_date = create_time, path = path)
        pic.save()


    class Meta(object):
        app_label = 'picture'
        db_table = 'picture_picture'





