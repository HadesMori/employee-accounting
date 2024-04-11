from django.db import models #type: ignore
from transliterate import slugify #type: ignore

# Create your models here.
class Employee(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True)
    age = models.SmallIntegerField(default=0, blank=True)
    address = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    education = models.CharField(max_length=30, blank=True)
    position = models.CharField(max_length=50)
    experience = models.SmallIntegerField(default=0, blank=True)
    salary = models.IntegerField()
    slug = models.SlugField(max_length=255, blank=True, unique=True, editable=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.last_name + "-" + self.first_name, language_code='uk')
        super(Employee, self).save(*args, **kwargs)