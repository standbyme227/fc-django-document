from django.db import models

__all__ = (
    'InstagramUser',
)


class InstagramUser(models.Model):
    name = models.CharField(max_length=50)
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        #대칭관계가 아님을 나타내기위해서 False
    )

    def __str__(self):
        return self.name