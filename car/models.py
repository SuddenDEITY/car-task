from django.db import models
from django.db.models.signals import pre_save,post_save,post_delete
from django.dispatch import receiver
from decimal import Decimal
from django.core.validators import MinValueValidator

class Car(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название автомобиля')
    manufacturer_charge = models.PositiveSmallIntegerField(verbose_name='Наценка производителя', default=0)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Общая стоимость', validators=[MinValueValidator(Decimal('0.00'))])
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
    
@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, *args, **kwargs):
    price = sum([el.total_price for el in instance.details.all()])
    instance.price = price + Decimal(instance.manufacturer_charge/100) * price




class Detail_Type(models.Model):
    type_name = models.CharField(max_length=100, verbose_name='Тип детали')

    def __str__(self) -> str:
        return self.type_name
    
    class Meta:
        verbose_name = 'Тип детали'
        verbose_name_plural = 'Типы деталей'



class Detail(models.Model):
    detail_type = models.ForeignKey(Detail_Type, on_delete=models.CASCADE, related_name='details', verbose_name='Тип детали')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Стоимость детали', validators=[MinValueValidator(Decimal('0.00'))])
    quantity = models.PositiveSmallIntegerField(verbose_name='Количество деталей', default=1)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='details', verbose_name='Автомобиль')
    total_price = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Общая стоимость', validators=[MinValueValidator(Decimal('0.00'))])

    def __str__(self) -> str:
        return self.detail_type.type_name
    
    class Meta:
        verbose_name = 'Деталь'
        verbose_name_plural = 'Детали'

@receiver(pre_save, sender=Detail)
def detail_pre_save(sender, instance, *args, **kwargs):
    instance.total_price = instance.price * instance.quantity

@receiver(post_save, sender=Detail)
def detail_post_save(sender, instance, *args, **kwargs):
    car = instance.car
    price = sum([el.total_price for el in car.details.all()])
    charge = Decimal(car.manufacturer_charge/100) * price
    car.price = price + charge
    car.save()

@receiver(post_delete, sender=Detail)
def detail_post_delete(sender, instance, **kwargs):
    car = instance.car
    price = sum([el.total_price for el in car.details.all()])
    charge = Decimal(car.manufacturer_charge/100) * price
    car.price = price + charge
    car.save()



class Extra(models.Model):
    detail_key = models.CharField(max_length=100, verbose_name='Параметр')
    detail_value = models.CharField(max_length=100, verbose_name='Значение')
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE, related_name='extras', verbose_name='Деталь')

    class Meta:
        verbose_name = 'Дополнение'
        verbose_name_plural = 'Дополнения'

    def __str__(self) -> str:
        return self.detail_key


