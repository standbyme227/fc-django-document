from django.db import models
from django.utils import timezone
from django.utils.datetime_safe import datetime

__all__ = (
    'Post',
    'User',
    'Postlike',
)


class Post(models.Model):
    title = models.CharField(max_length=50)
    like_users = models.ManyToManyField(
        'User',
        through='PostLike',
        related_name='like_post',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'intermediate - Post'


class User(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'intermediate - User'


class Postlike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return f'"{self.post.title}"글의 좋아요({self.user.name}, {self.created_date})'
        return f'"{title}"글의 좋아요({name}, {date})'.format(
            title=self.post.title,
            name=self.user.name,
            date=datetime.strftime(
                timezone.localtimee(self.created_date),
                '%Y.%m.%d')
        )

    class Meta:
        verbose_name_plural = 'intermediate - Postlike'