from django.db import models

# Create your models here.
class Result(models.Model):
    amount = models.FloatField()
    tip_percent = models.IntegerField(help_text="%")

    def calculate(self):
        result =  self.amount * self.tip_percent / 100
        result = f"{result:.2f}"
        return result