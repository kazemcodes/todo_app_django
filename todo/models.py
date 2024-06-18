from django.db import models
from django.contrib.auth.models import User
from PIL import Image
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['completed']
        

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    
    avatar = models.ImageField(
        default='avatar.jpg', # default avatar
        upload_to='profile_avatars',
    )
    def __str__(self) -> str:
        return f'{self.user.username} Profile'
    def save(self, *args, **kwargs):
        super().save( *args, **kwargs)
        
        img = Image.open(self.avatar.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            # create a thumbnail
            img.thumbnail(output_size)
            # overwrite the larger image
            img.save(self.avatar.path)