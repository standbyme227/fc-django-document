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
        related_name='followers'
    )

    class Meta:
        verbose_name_plural = 'symmetrical - InstagramUser'

    def __str__(self):
        return self.name

    # def followers(self):
    #     followers_string = ', '.join([follower.name for follower in self.following.all()])
    #     #역참조 뭐긴아니???? 원하는 것을 소문자화 + _ + set
    #     return '{name} (팔로워: {followers})'.format(
    #         name=self.name,
    #         followers=followers_string,
    # )
