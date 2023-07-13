from django.db import models

class Author(models.Model):
    name = models.CharField()
    bio = models.TextField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField()
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category)
   

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.author} on {self.post}: {self.content[:50]}"
