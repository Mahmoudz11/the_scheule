from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError

from accounts.models import User


days = (('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'))

hours = (('8','8'),
         ('9','9'),('9.30','9.30'),
         ('10','10'),('10.30','10.30'),
         ('11','11'),('11.30','11.30'),
         ('12','12'),('12.30','12.30'),
         ('13','13'),('13.30','13.30'),
         ('14','14'),('14.30','14.30'),
         ('15','15'),('15.30','15.30'),
         ('16','16'),('16.30','16.30'),
         ('17','17'),('17.30','17.30'),
         ('18','18'),('18.30','18.30'),
         ('19','19'),('19.30','19.30'),
         ('20','20'))

location = (('main hall','main hall'),
            ('class 201', 'class 201'),
            ('class 202', 'class 202'),
            ('class 203', 'class 203'),
            ('class 204', 'class 204'),
            ('class 205', 'class 205') )

class Course(models.Model):
    instructor_name = models.ForeignKey(User, on_delete=models.CASCADE)
    course_name     = models.CharField(max_length=250)
    day             = models.CharField(max_length=9, choices=days)
    from_hour       = models.CharField(max_length=5, choices=hours)
    to_hour         = models.CharField(max_length=5, choices=hours)
    location        = models.CharField(max_length=50, choices=location)

    def __str__(self):
        return f'{self.course_name} Course by {self.instructor_name} on {self.day} in {self.location} from {self.from_hour} to {self.to_hour}'

    def get_absolute_url(self):
        return reverse('schedule:detail', kwargs={'pk':self.pk})


class FinalSchedule(models.Model):
    user        = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    schedule    = models.ManyToManyField(Course)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user

    def get_absolute_url(self):
        return reverse('schedule:final-detail', kwargs={'pk':self.pk})
