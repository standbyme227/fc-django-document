from django.db import models


__all__ = (
    'FacebookUser',
)

class FacebookUser(models.Model):
    name = models.CharField(max_length=50)
    friends = models.ManyToManyField('self')

    def __str__(self):
        friends_string = ', '.join([friend.name for friend in self.friends.all()])

        return '{name} (친구: {friends})'.format(
            name=self.name,
            friends=friends_string,
        )

    class Meta:
        verbose_name_plural = 'self - FacebookUser'

