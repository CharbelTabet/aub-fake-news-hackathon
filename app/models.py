from django.db import models
from django.utils.timezone import now

class Threat(models.Model):
    title = models.CharField(max_length=140)
    description = models.CharField(max_length=140)
    who = models.CharField(max_length=140)
    what = models.CharField(max_length=140)
    where = models.CharField(max_length=140)
    when = models.CharField(max_length=140) 
    why = models.CharField(max_length=140)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # topic = models.ForeignKey(Topic, on_delete=models.SET_NULL)

    def getTestimonies(self, choice=None):
        if choice in [True, False]:
            return Testimony.objects.filter(threat=self, choice=choice)
        return Testimony.objects.filter(threat=self)

    def getChoices(self, choice=None):
        if choice in [True, False]:
            return Testimony.objects.filter(threat=self, choice=choice).count()
        return Testimony.objects.filter(threat=self).count()
    
    def __str__(self):
        return self.who

class Testimony(models.Model):
    threat = models.ForeignKey(Threat, on_delete=models.CASCADE)
    choice = models.BooleanField(choices=[
        (True, 'Approve'),
        (False, 'Disapprove')
    ])
    comment = models.TextField(max_length=100)
    def __str__(self):
        return 'Testimony for: {}'.format(self.threat)

class Topic(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=40)
    def __str__(self):
        return '{}'.format(self.title)
