from _decimal import Decimal

from django.db import models


# Create your models here.
class Song(models.Model):
    index = models.IntegerField(primary_key=True)
    id = models.CharField(max_length=255)
    title = models.TextField()
    danceability = models.DecimalField(max_digits=20, decimal_places=10)
    energy = models.DecimalField(max_digits=20, decimal_places=10)
    mode = models.IntegerField()
    acousticness = models.DecimalField(max_digits=20, decimal_places=10)
    tempo = models.DecimalField(max_digits=20, decimal_places=10)
    duration_ms = models.IntegerField()
    num_sections = models.IntegerField()
    num_segments = models.IntegerField()
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    ratings_count = models.IntegerField(default=0)

    def add_rating(self, new_rating):
        new_rating = Decimal(new_rating)

        total_rating = self.average_rating * Decimal(self.ratings_count)

        # Update count and recalculate the average
        self.ratings_count += 1
        self.average_rating = (total_rating + new_rating) / Decimal(self.ratings_count)
        self.save()

    def __str__(self):
        return self.title
