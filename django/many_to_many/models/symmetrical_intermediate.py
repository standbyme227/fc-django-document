from django.db import models

class TwitterUser(models.Model):
    name = models.Charfield(max_length=50)

    #일방적인계아니라 관계를 설정해야해서 following으로 하지 않았다.
    relations = models.ManyToManyField(
        'self',
        symmetrical=False,
        through='Relation',
        related_name='+',
    )


class Relation(models.Model):
    '''
    유저간의 관계를 정의하는 모델
    단순히 자신의 MTM이 아닌 중개모델의 역할을 함
    추가적으로 받는 정보는 관계의 타입(팔로잉 또는 차단)
    '''
    RELATION_TYPE_FOLLOWING = 'f'
    RELATION_TYPE_BLOCK = 'b'
    CHOICES_TYPE = (
        (RELATION_TYPE_FOLLOWING, '팔로잉'),
        (RELATION_TYPE_BLOCK, '차단'),
    )
    from_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE
    )
    to_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE
    )
    type = models.CharField(max_length=1, choices=CHOICES_TYPE)
