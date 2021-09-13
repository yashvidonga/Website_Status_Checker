from django.db import models


class websiteurl(models.Model):
    url_id = models.AutoField(primary_key=True)
    web_name = models.CharField(max_length=50, default="")
    status = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.web_name


class FilesUpload(models.Model):
    file = models.FileField()
