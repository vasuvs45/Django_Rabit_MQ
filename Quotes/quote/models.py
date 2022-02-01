from django.db import models

# Create your models here.
class Quote(models.Model):
    title = models.CharField(max_length=50)

    likes = models.PositiveIntegerField(default=0)

    def __dir__(self):
        return self.title

# class User (models.Model):

#     class Meta:
#         verbose_name = _("")
#         verbose_name_plural = _("s")

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("_detail", kwargs={"pk": self.pk})
