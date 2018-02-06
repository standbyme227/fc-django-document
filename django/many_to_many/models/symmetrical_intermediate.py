from django.db import models


__all__ = (
    'TwitterUser',
    'Relation',
)


class TwitterUser(models.Model):
    name = models.CharField(max_length=50)

    #일방적인계아니라 관계를 설정해야해서 following으로 하지 않았다.
    relations = models.ManyToManyField(
        'self',
        symmetrical=False,
        through='Relation',
        related_name='+',
    )
    def __str__(self):
        return self.name


    def following(self):
        # 내가 from_user이며 , type이 팔로잉인 Relation의 쿼리
        following_relations = self.relations_by_from_user.filter(
            type=Relation.RELATION_TYPE_FOLLOWING,
        )
        #위에서 정제한 쿼리셋에서 'pk'값만 리스트로 가져옴 (내가 팔로잉하는 유저의 pk리스트)
        following_pk_list = following_relations.values_list('to_user', flat=True)
        #TwitterUser테이블에서 pk가
        #바로 윗줄에서 만든 following_pk_list

        following_users = TwitterUser.objects.filter(pk__in=following_pk_list)
        return following_users

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
    #단순한 텍스트를 받고 실제쓰는 것을 따로 규정


    from_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        related_name='relations_by_from_user',
    )
    to_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        related_name='relations_by_to_user',
    )
    #related_name을 설정한 이유는 각각의 reverse의 네임이 하나의 클래스를 통해서 구성되기에 충돌이 일어나기때문이다.
    #from_user의 반대는 Relation_Set이고 to_user도 마찬가지이다.
    type = models.CharField(max_length=1, choices=CHOICES_TYPE)
