from django.db import models

class Confession(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Confession {self.id} on {self.date_posted}'
