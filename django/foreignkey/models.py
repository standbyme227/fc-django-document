from django.db import models




class Car(models.Model):
    manufacturer = models.ForeignKey(
        'Manufacturer', #문자열로 처리전에는 Manufacturer클래스가 아래에 있어서 참조를 못했었다.
        on_delete=models.CASCADE,
        verbose_name='제조사'
    )
    name = models.CharField('모델명', max_length=60)

    def __str__(self):
        return(f'{self.manufacturer}{self.name}')
        pass


class Manufacturer(models.Model):
    name = models.CharField('제조사명',max_length=50)

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=60)
    teacher = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL, #만약에 CASCADE를 한다면 지정된 사람에 대해서 같이 삭제된다.
        null=True,
        blank=True,
    )




class Type(models.Model):
    type_number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)

    def __str__(self):
        return f'{self.type_number}| {self.name}'

class Pokemon(models.Model):
    dex_number = models.IntegerField(primary_key=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.dex_number:03}. {self.name} {self.type.name}'