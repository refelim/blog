from django.db import models
from django.conf import settings

class Tag(models.Model) :
    name = models.CharField(max_length=50, blank=True, unique=True)

    def __str__(self) : 
        return self.name
    
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    contents = models.TextField()
    tags = models.ManyToManyField('Tag', blank = True)
    img = models.ImageField(upload_to= 'blog/%Y/%m/%d/', blank = True)
    created_at = models.DateTimeField(auto_now_add = True , null = True) # 처음 생성될 때에만
    updated_at = models.DateTimeField(auto_now = True) # 수정될 때마다
    

    def __str__(self):
        tags = self.tags
        create_time = self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        update_time = self.updated_at.strftime("%Y-%m-%d %H:%M:%S")
        return f"제목: {self.title}, 생성시간: {create_time}, 수정시간: {update_time}"
