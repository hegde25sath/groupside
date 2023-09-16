from django.db import models

class Student(models.Model):
    name = models.charField(max_length=100)

    FRESHMAN = "FR"
    SOPHOMORE = "SO"
    JUNIOR = "JR"
    SENIOR = "SR"
    GRADUATE = "GR"
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, "Freshman"),
        (SOPHOMORE, "Sophomore"),
        (JUNIOR, "Junior"),
        (SENIOR, "Senior"),
        (GRADUATE, "GRADUATE"),
    ]
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default = FRESHMAN,
    )
    notes = models.CharField(max_length=200, 
                             default="Any other comments or information you would like others to know? ")
