from django.db import models
from django.utils import timezone

# Create your models here.

class itemTodo(models.Model):
    desc = models.TextField(max_length=200)
    done = models.BooleanField(default=False)

    def __str__(self):
        if(len(self.desc) > 18):
            return str(self.id) + ": " + self.desc[:18] + '... ' + str(self.done)
        return str(self.id) + ": " + self.desc + ' ' + str(self.done)
