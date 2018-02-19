from django.db.models.manager import Manager

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    is_block = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class AdminManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_admin=True)
# 이건 말그대로 쿼리셋을 필터하는 부분으로
# 인스턴스가 is_admin에 대해서 True이면 나오게 걸러주는 그런 코딩이다.


class Admin(User):
    admin_objects = AdminManager()
    # 원래 기본 manager의 default값이 objects다.


    class Meta:
        proxy = True

    def __str__(self):
        return f'{self.name} (관리자)'

    @staticmethod
    def drop(user):
        user.delete()


class StaffManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_staff=True)

# 이건 말그대로 쿼리셋을 필터하는 부분으로
# 인스턴스가 is_staff에 대해서 True이면 나오게 걸러주는 그런 코딩이다.


class Staff(User):
    objects = StaffManager()


    class Meta:
        proxy = True

    def __str__(self):
        return f'{self.name} (스태프)'

    @staticmethod
    def block(user):
        user.is_block = True
        user.save()