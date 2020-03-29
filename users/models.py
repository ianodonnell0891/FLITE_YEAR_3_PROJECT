from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(default='melodia_logo.png',
                                    upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.profile_img.path)

        if img.height or img.width > 300:
            display_size = (300, 300)
            img.thumbnail(display_size)
            img.save(self.profile_img.path)


