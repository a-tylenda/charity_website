from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name}"

class Institution(models.Model):
    FUNDACJA = 0
    ORGANIZACJA_POZARZADOWA = 1
    ZBIORKA_LOKALNA = 2

    TYPE = {
    (FUNDACJA, 'Fundacja'),
    (ORGANIZACJA_POZARZADOWA, 'Organizacja Pozarządowa'),
    (ZBIORKA_LOKALNA, 'Zbiórka lokalna'),
}

    name = models.CharField(max_length=128)
    description = models.TextField(null=True)
    type = models.IntegerField(choices=TYPE, default=FUNDACJA)
    categories = models.ManyToManyField("Category")

    def __str__(self):
        return f"{self.name}"

class Donation(models.Model):
    quantity = models.SmallIntegerField()
    categories = models.ManyToManyField("Category")
    institution = models.ForeignKey("Institution", on_delete=models.CASCADE)
    address = models.CharField(max_length=256)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=256)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return f"{self.user.username} {self.categories.name} {self.quantity}"