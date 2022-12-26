from djongo import models

# Create your models here.

class Verse(models.Model):
    id = models.ObjectIdField()
    verse = models.IntegerField()

class Memo(models.Model):
    id = models.ObjectIdField()
    userID = models.CharField(max_length=100)
    book = models.CharField
    cardColor = models.CharField
    chapter = models.IntegerField
    createdAt = models.DateField
    memo = models.TextField
    textColor = models.CharField
    verses = models.ArrayField(
        model_container= Verse,
    )
    objects = models.DjongoManager()


