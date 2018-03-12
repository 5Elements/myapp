from django.db import models
import datetime


# Create your models here.
class Tweet(models.Model):
	created_date = models.TextField()
	user = models.TextField()
	text = models.TextField()
	coordinates = models.TextField(null=True)

        #To view the stored tweets
	def __str__(self):
                result = ""
                if self.coordinates is None:
                        result += self.created_date+"-->"+" "+"-->"+self.user+"-->"+self.text
                else:
                        result += self.created_date+"-->"+self.coordinates+"-->"+self.user+"-->"+self.text
                return result
	


