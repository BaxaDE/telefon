from django.urls import reverse
from django.db import models
from ckeditor.fields import RichTextField
from PIL import Image


# Create your models here.
class TelefonlarModels(models.Model):
    full_name = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    oyiga = models.CharField(max_length=50)

    class Meta:
        verbose_name = "telefon"
        verbose_name_plural = "telefonlar"

    def __str__(self):
        return self.full_name

    @property
    def rasmlar(self):
        return self.images.all()

    @property
    def asos(self):
        return self.rasmlar.first()

    @property
    def chegirmadami(self):
        return self.chegirmalar_set.all()

    @property
    def chegirma_narxi(self):
        if self.chegirmadami:
            return (100 - self.chegirmadami.foizi) / 100 * float(self.oyiga)

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_id": self.pk})

    # tel rasmlar
class Tel_Rasmlari(models.Model):
    telefon = models.ForeignKey(TelefonlarModels, on_delete=models.CASCADE, related_name="images")
    rasm = models.ImageField(upload_to="tel_rasmlari")

    class Meta:
        verbose_name = "Tel Rasmlari"


class Chegirmalar(models.Model):
    foizi = models.IntegerField("Chegirma foiz miqdorida")
    telefonlar = models.ManyToManyField(TelefonlarModels, null=True)

    class Meta:
        verbose_name = "Chegirmalar"
        verbose_name_plural = "Chegirmalar"


# xarakteristika telefon
class XarakteristikaModels(models.Model):
    joylashuv = models.CharField(max_length=50)
    kredit_12oy = models.CharField(max_length=50)
    kredit_6oy = models.CharField(max_length=50)
    kredit_xujat = models.CharField(max_length=100)
    yetkazib_berish = models.CharField(max_length=50)
    oldindan_tulov = models.CharField(max_length=50)
    tel_raqam1 = models.CharField(max_length=50, null=True, blank=True)
    tel_raqam2 = models.CharField(max_length=50, null=True, blank=True)
    telefon = models.OneToOneField(
        TelefonlarModels,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.telefon.full_name

    class Meta:
        verbose_name = 'Xarakteristika'
        verbose_name_plural = 'Xarakteristikalar'

    def save(self):
        return super(XarakteristikaModels, self).save()

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_id": self.pk})


class XususiyatModels(models.Model):
    title = models.CharField(max_length=100)
    batafsil = models.TextField()
    tel = models.OneToOneField(
        TelefonlarModels,
        on_delete=models.CASCADE,

    )

    def __str__(self):
        return self.title


class Bizhaqimizda(models.Model):
    description = RichTextField(config_name="default")

class IjtimoitarmoqModels(models.Model):
    e_mail = models.CharField(max_length=50)
    tel_raqam1 = models.CharField(max_length=50, null=True, blank=True)
    tel_raqam2 = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = 'ijtimoitarmoq'
        verbose_name_plural = 'ijtimoitarmoqlar'

    def save(self):
        return super(IjtimoitarmoqModels, self).save()

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_id": self.pk})


