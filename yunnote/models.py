from enum import unique
from django.db import models

# Create your models here.


# 分组
class Group(models.Model):
    id = models.AutoField('分组ID', primary_key=True)
    name = models.CharField('分组名称', null=False, unique=True, max_length=20)
    sort_no = models.IntegerField('排序', null=True)

    class Meta:
        verbose_name = '分组'


# 笔记
class Note(models.Model):
    id = models.AutoField('笔记ID', primary_key=True)
    name = models.CharField('笔记名称', null=False, max_length=20)
    group_id = models.IntegerField('分组ID', null=True)
    sort_no = models.IntegerField('排序')
    content = models.TextField('笔记内容', max_length=2048000)

    class Meta:
        verbose_name = '笔记'
        # unique_together = (('group_id', 'sort_no'))
