from django.db import models
from django.db.models import Manager


class Person(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    # objects가 Manager로 생성됨


class NewManager(Manager):
    def get_queryset(self):
        print('NewManager get_queryset')
        return super().get_queryset()
    # Manager의 명칭을 NewManager로 바꿈
    # Person에 영향을 주는게 아님




class MyPerson1(Person):
    secondary = NewManager()
    class Meta:
        proxy = True
    # secondary하면 Newmanager를 실행시켜서 Manager를 NewManager로 바꿈


class ExtraManagerModel(models.Model):
    secondary = NewManager()

    class Meta:
        abstract = True
    # secondary하면 Newmanager를 실행시켜서 Manager를 NewManager로 바꿈
    # 거기다가 _default_manager 까지 바꿈.


class MyPerson2(Person, ExtraManagerModel):
    class Meta:
        proxy = True

