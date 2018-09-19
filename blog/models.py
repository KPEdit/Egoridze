from django.db import models


class User(models.Model):
    name = models.CharField(max_length=256, help_text="Имя пользователя")
    surname = models.CharField(max_length=256, help_text="Фамилия пользователя")

    def __str__(self):
        return "%s %s"%(self.name, self.surname)


class Article(models.Model):
    title = models.CharField(max_length=256)
    author = models.OneToOneField(User, models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    blog = models.TextField()

    def __str__(self):
        return self.title

