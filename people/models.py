from django.db import models

def nt_id_default():
    return {"nt_id":"NT ID Default"}

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    department = models.CharField(max_length=16)
    position = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    nt_id = models.CharField(default=nt_id_default, max_length=32)

class User(models.Model):
    GROUP_EnterISTeam = 'Enterprise IS Team'
    GROUP_EngEnable = 'Engineering Enablement'
    GROUP_EmdID = 'Emdedded IT'
    GROUP_NAME_CHOICE = [
        (GROUP_EnterISTeam, 'Enterprise IS Team'),
        (GROUP_EngEnable, 'Engineering Enablement'),
        (GROUP_EmdID, 'Emdedded IT'),
    ]
    user_nt_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    group_name = models.CharField(blank=True, choices=GROUP_NAME_CHOICE, max_length=16)

class Subject_Matter_Expert(models.Model):
    sme_nt_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    title = models.CharField(max_length=16)
    responsibility = models.CharField(max_length=32)

