from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100, blank=True)


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField(blank=True, null=True,)
    num_stars = models.IntegerField()

class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )

    name = models.CharField('이름', max_length=60)
    # nickname = models.CharField(
    #     max_length=30,
    #     unique=True
    # )
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)


    def __str__(self):
        # 이한영 (PK: 1, 셔츠 사이즈: Medium)
        return '{name} (PK: {pk}, 셔츠 사이즈: {shirt_size}'.format(
            name=self.name,
            pk=self.pk,
            shirt_size=self.get_shirt_size_display(),
        )