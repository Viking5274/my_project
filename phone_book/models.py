from django.db import models
from django.urls import reverse


class PhoneBook(models.Model):
    name = models.CharField('Name', max_length=50)
    surname = models.CharField('Surname', max_length=65)
    address_country = models.CharField('Country', max_length=255)
    address_city = models.CharField('City', max_length=255)
    address_street = models.CharField('Street', max_length=255)
    url = models.URLField("URL")
    phone = models.CharField("Phone", max_length=15)
    pic = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.name + '|' + self.surname

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def get_absolute_url(self):
        return reverse('user-details', args=[str(self.id)])

