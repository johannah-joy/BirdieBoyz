from django.db import models
from django.utils import timezone
from django import forms
from datetime import date

# Create your models here.

class Birdie(models.Model):
    players =(
        ("Bryan", "Bryan"),
        ("David", "David"),
        ("Greg", "Greg"),
        ("Steve", "Steve"),
    )
    player = models.CharField(max_length=10, null=True, blank=True, choices = players)
    date = models.DateField(null=True)
    courses =(
        ("Broadmoor", "Broadmoor"),
        ("Camas Meadows", "Camas Meadows"),
        ("Colwood", "Colwood"),
        ("Heron Lakes Great Blue", "Heron Lakes Great Blue"),
        ("Heron Lakes Greenback", "Heron Lakes Greenback"),
        ("Lewis River", "Lewis River"),
        ("Riverside Golf Club", "Riverside Golf Club"),
        ("Tri Mountain", "Tri Mountain"),
        ("Other", "Other"),
    )
    course = models.CharField(max_length=100, null=True, blank=True, choices = courses)
    holes =( 
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
        (6, "6"),
        (7, "7"),
        (8, "8"),
        (9, "9"),
        (10, "10"),
        (11, "11"),
        (12, "12"),
        (13, "13"),
        (14, "14"),
        (15, "15"),
        (16, "16"),
        (17, "17"),
        (18, "18"),
    )
    hole = models.IntegerField(null=True, blank=True, choices = holes)

    def __str__(self):
        return f'{self.player}, {self.date}, {self.course}, {self.hole}'