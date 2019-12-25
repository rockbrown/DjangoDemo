from django.db import models

# Create your models here.
class Mst_Post_Statuses(models.Model):
    code = models.CharField(primary_key=True, max_length=32)
    label = models.CharField(max_length=255)
    is_enabled = models.IntegerField(default=0)

    def __str__(self):
        return self.label


class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    post_status_code = models.ForeignKey(Mst_Post_Statuses, on_delete=models.CASCADE)
    created = models.DateTimeField('date published')
    modified = models.DateTimeField('date published')

    def __str__(self):
        return self.title
