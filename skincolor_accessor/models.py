from django.db import models

class undertone(models.Model):
    u_tone = models.CharField(max_length=250)

    def __str__(self):
        return self.u_tone

class skintone(models.Model):
    s_tone = models.CharField(max_length=250)
    example_photo = models.CharField(max_length=1000)

    def __str__(self):
        return self.s_tone
