from django.db import models

class ItemModel(models.Model):
    id = models.AutoField('id', primary_key=True)
    name = models.CharField('name', max_length=128)
    category = models.CharField('category', max_length=128)
    created_at = models.DateTimeField('create time', auto_now_add=True)

    class Meta:
        db_table = 'items'