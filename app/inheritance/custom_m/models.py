from django.db import models
from django.db.models import Manager


class CustomManager(Manager):
    def get_queryset(self):
        print('Custom manger get_queryset!')
        return super().get_queryset()

class OtherManager(Manager):
    def get_queryset(self):
        print('Other manger get_queryset!')
        return super().get_queryset()


class AbstractBase(models.Model):
    objects = CustomManager()

    class Meta:
        abstract = True



class ChildA(AbstractBase):
    pass



class ChildB(AbstractBase):
    default_manager = OtherManager()



class ExtraManagerModel(models.Model):
    extra_manager = OtherManager()

    class Meta:
        abstract = True


class ChildC(AbstractBase, ExtraManagerModel):
    pass

class ChildD(ExtraManagerModel):
    pass