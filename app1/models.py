from __future__ import unicode_literals

from django.db import models
from django import forms




class Kitap(models.Model):
    baslik=models.CharField(max_length=70)
    class Meta:
     verbose_name = "Kitap"
     verbose_name_plural = 'Kitaplar'


def __str__(self):
	return self.baslik

class Yazar(models.Model):
	isim=models.CharField(max_length=30)
	soyisim=models.CharField(max_length=30)
	kitaplar=models.ManyToManyField(Kitap)

def __str__(self):
    return '%s %s'%(self.isim,self.soyisim)