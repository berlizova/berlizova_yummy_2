from django.db import models
from django.utils.text import slugify
from django.core.validators import RegexValidator


# Create your models here.
def generate_slug(name):
    return slugify(name)


class DishCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    is_visible = models.BooleanField(default=True)
    sort = models.PositiveSmallIntegerField()
    slug = models.SlugField(max_length=255, default='', blank=True)

    # Override save method to generate slug automatically
    def save(self, *args, **kwargs):
        # If slug is not provided, generate it from name
        if not self.slug:
            self.slug = generate_slug(self.name)
        super().save(*args, **kwargs)

    def __iter__(self):
        for dish in self.dishes.filter(is_visible=True):
            yield dish

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория блюд'
        verbose_name_plural = 'Категории блюд'
        ordering = ['sort']


class Staff(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='staff_photo/', blank=True, null=True)
    bio = models.TextField()  # field for staff biography
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Restaurant Staff'
        verbose_name_plural = 'Restaurant Staff'


class Dish(models.Model):
    name = models.CharField(max_length=255, unique=True)
    ingredients = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_visible = models.BooleanField(default=True)
    category = models.ForeignKey(DishCategory, on_delete=models.CASCADE, related_name='dishes')
    sort = models.PositiveSmallIntegerField()

    photo = models.ImageField(upload_to='dishes/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Dish'
        verbose_name_plural = 'Dishes'
        ordering = ['sort']


class Gallery(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = 'photos'
        ordering = ['name']


class Events(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    photo = models.ImageField(upload_to='events/', blank=True, null=True)
    sort = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        ordering = ['sort']


class Contacts(models.Model):
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    opening_hours = models.TextField()

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


class Reservation(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. "
                                         "Up to 15 digits allowed.")

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, validators=[phone_regex])
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    count = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True, null=True)

    is_confirmed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.date} {self.time}'

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'reservations'
        ordering = ('-date_created', )
