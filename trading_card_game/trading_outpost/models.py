from django.db import models



class Queens(models.Model):
    name= models.CharField(max_length= 100)
    winner= models.BooleanField()
    missCongeniality= models.BooleanField()
    quote= models.TextField()
    image_url= models.URLField(null=True)

    def __str__(self):
        return self.name

class My_Card(models.Model):
    STATUS_CHOICE= [
        ('O','Open'),
        ('C','Closed'),
        ('G','Give')]
    queen= models.ForeignKey(Queens, on_delete=models.CASCADE) 
    #Should link the card object
    profile= models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
    status= models.CharField(choices= STATUS_CHOICE, max_length=50, default='C')

    def __str__(self):
        return self.queen





