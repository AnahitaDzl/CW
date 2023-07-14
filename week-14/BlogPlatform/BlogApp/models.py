from django.db import models
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'title: {self.title} | author: {self.author} | publish date: {self.date}'

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self) -> str:
        return f'name:{self.name} | description:{self.bio}'


class Comment(models.Model):
    post = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self) -> str:
        return f'name:{self.name} | description:{self.description}'
