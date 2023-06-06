from django.db import models

class Unit(models.Model):
    """ Единица измерения """
    name = models.CharField(max_length=100, verbose_name="Именование", null=True, blank=False, unique=True)
    slug = models.CharField(max_length=10, verbose_name="Сокращенное именование", null=True, blank=False, unique=True)
    is_integer = models.BooleanField(default=False, verbose_name="Целочисленная единица измерения?", help_text="Например - штука")

    def __str__(self):
        return self.name
    
    def get_slug(self):
       return str(self.slug).lower() 
    

class Product(models.Model):
    """ Товар, материал """
    name = models.CharField(max_length=200, verbose_name="Название")
    quantity = models.FloatField(default=0, verbose_name="Количество")
    last_updated = models.DateTimeField(auto_now=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, null=True, verbose_name="Единица измерения")

    def __str__(self):
        return self.name
    
    def get_quantity(self):
        """ Округляет целочисленные единицы """
        if self.unit.is_integer:
            return int(self.quantity)
        return self.quantity
    
    # def is_unique
    def get_datetime(self):
        return self.last_updated.strftime("%d-%m-%Y в %H:%M")
    
    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super(Product, self).save(*args, **kwargs)


    


