from django.db import models

class Author(models.Model):
    name = models.CharField()
    bio = models.TextField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField()
    description = models.TextField()
    

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField()
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.author} on {self.post}: {self.content[:50]}"
