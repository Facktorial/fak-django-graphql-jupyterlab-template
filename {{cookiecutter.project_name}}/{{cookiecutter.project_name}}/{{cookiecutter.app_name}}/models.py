from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Test(models.Model):
    """
    Model to be erased in a while.
    """
    name = models.CharField(
        default="IS MY PORPOISE TO BE TESTES?",
        max_length=64,
        verbose_name="name"
    )

    size = models.IntegerField(
        default=8,
        validators=[MaxValueValidator(10), MinValueValidator(0)],
        verbose_name="power",
    )

    consumers = models.CharField(
        max_length = 1024,
        default="",
    )    
    
    def __str__(self):
        return self.name