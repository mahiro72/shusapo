from django.db import models
from django.contrib.auth import get_user_model


user = get_user_model()

class Comment(models.Model):
    post_user = models.ForeignKey(user, on_delete=models.PROTECT)
    main = models.CharField(max_length=30)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.main+"("+str(self.post_user)+")"

    class Meta:
        ordering = ('-date',)
        
