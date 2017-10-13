from django.db import models
from django.contrib import admin
from multiselectfield import MultiSelectField


# Create your models here.
class BioData(models.Model):
    full_name = models.CharField("Full name:", max_length=60, blank=True)
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField("Gender:", max_length=1, choices=GENDER, blank=True)
    MARITAL_STATUS = (
        ('S', 'Single'),
        ('M', 'Married'),
        ('W', 'Widow'),
        ('W', 'Widower'),
        ('Se', 'Separated'),
    )
    marital_status = models.CharField("Marital Status:", max_length=2, choices=MARITAL_STATUS, blank=True)
    phone = models.CharField("Phone:", max_length=100, blank=True)
    town = models.CharField("Town:", max_length=100, blank=True)
    lga = models.CharField("LGA:", max_length=100, blank=True)
    state = models.CharField("State of Origin:", max_length=100, blank=True)
    email = models.EmailField("Email Address: (example: abc@example.com)", max_length=200, blank=True)
    residence = models.CharField("Home Address:", max_length=300, blank=True)
    name_of_next_of_kin = models.CharField("Name of next of Kin:", max_length=100, blank=True)
    address_of_next_of_kin = models.CharField("Address of next kin:", max_length=200, blank=True)
    relation_with_next_of_kin = models.CharField("Relationship with next of kin:", max_length=100, blank=True)

    def __str__(self):
        return self.full_name


class Specialization(models.Model):
    occupation = models.CharField("Occupation:", max_length=100, blank=True)
    business_address = models.CharField("Business Address:", max_length=200, blank=True)
    skills = models.CharField("Skills/Talents:", max_length=100, blank=True)
    sports = models.CharField("Sports:", max_length=100, blank=True)

    def __str__(self):
        return self.occupation


class SpiritualData(models.Model):
    BAPTIZED = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    are_you_a_baptized_catholic = models.CharField("Are you a babtized catholic ?", max_length=1, choices=BAPTIZED,
                                                   blank=True)
    not_baptized = models.CharField("If no, please, state your reasons:", max_length=300, blank=True)

    COMMUNICANT = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    are_you_a_communicant = models.CharField("Are you a communicant ? ", max_length=1, choices=COMMUNICANT, blank=True)
    not_communicant = models.CharField("If no, please, state your reasons", max_length=300, blank=True)

    CONFIRMED_CATHOLIC = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    are_you_confirmed = models.CharField("Are you confirmed ? ", max_length=1, choices=CONFIRMED_CATHOLIC, blank=True)
    not_confirmed = models.CharField("If no, please, state your reasons:", max_length=300, blank=True)

    WEDDED = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    are_wedded_in_the_church = models.CharField("Are you wedded in the church ? ", max_length=1, choices=WEDDED, blank=True)
    not_wedded = models.CharField("If no, please, state your reasons:", max_length=300, blank=True)

    TRIBAL_COMMUNITY = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    any_tribal_community = models.CharField("Do you belong to any tribal communities in the church ? ", max_length=1, choices=CONFIRMED_CATHOLIC, blank=True)
    not_in_tribal_community = models.CharField("If no, please, state reasons:", max_length=300, blank=True)
    in_tribal_community = models.CharField("If yes, please, state the community:", max_length=300, blank=True)

    PIUS_SOCIETY = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    member_of_any_pius_society = models.CharField("Are you a member of any pius societies in the church ? ", max_length=1, choices=PIUS_SOCIETY, blank=True)
    not_in_pius_society = models.CharField("If no, please state your reasons:", max_length=300, blank=True)
    yes_In_pius_society = models.CharField("If yes, please, state the society:", max_length=300, blank=True)

    ORGAN_CHURCH = (
        ('W', 'CWO'),
        ('M', 'CMO'),
        ('C', 'CYON'),
    )
    belongs_to_any_organ_in_church = models.CharField("Do you belong to any of the three organs in the church ?", max_length=1, choices=ORGAN_CHURCH, blank=True)
    dont_belong_to = models.CharField("If no, please state reasons:", max_length=300, blank=True)
    yes_belong_to = models.CharField("If yes, please, state the organ:", max_length=300, blank=True)

    def __str__(self):
        return self.are_you_a_baptized_catholic


class ChurchWorkHistory(models.Model):
    # def __init__(self):
    #     self.catechetical_work

    CATECHETICAL_WORK = (
        ('a', 'Teaching Catechisms'),
        ('b', 'Teaching in sunday school'),
        ('c', 'Teaching in marriage course'),
        ('d', 'Infant Baptism class'),
    )

    LITURGICAL_WORK = (
        ('a', 'Choir'),
        ('b', 'Proclamation(Layreader/Lector)'),
        ('c', 'Church wardens'),
        ('d', 'Alter Service'),
    )

    SECURITY_WORK = (
        ('a', 'MOD'),
        ('b', 'Boys Brigade'),
        ('c', 'Security committee'),
        ('d', 'Not apply'),
    )

    ENVIRONMENTAL_WORK = (
        ('a', 'Personal church cleaning'),
        ('b', 'Gardenning'),
        ('c', 'Societal church cleaning'),
        ('d', 'Not apply'),
    )

    HEALTH_WORK = (
        ('a', 'Health committee'),
        ('b', 'Medical practitioner'),
        ('c', 'Midwifing'),
        ('d', 'Other, please specify'),
    )

    SPORTS = (
        ('a', 'Sports committee'),
        ('b', 'Trainer/Coach'),
        ('c', 'Umpire'),
        ('d', 'Sport team'),
    )

    OTHER_WORK = (
        ('a', 'Harvest and Bazaar'),
        ('b', 'Fund raising'),
        ('c', 'Building/Project'),
        ('d', 'Enlightenment and Awareness'),
        ('e', 'Finance'),
        ('f', 'Other, please specify'),
    )
    catechetical_work = MultiSelectField(max_length=5, choices=CATECHETICAL_WORK, blank=True)
    liturgical_work = MultiSelectField(max_length=5, choices=LITURGICAL_WORK, blank=True)
    security_work = MultiSelectField(max_length=5, choices=SECURITY_WORK, blank=True)
    environmental_work = MultiSelectField(max_length=5, choices=ENVIRONMENTAL_WORK, blank=True)
    health_work = MultiSelectField(max_length=4, choices=HEALTH_WORK, blank=True)
    sports = MultiSelectField(max_length=5, choices=SPORTS, blank=True)
    other_work = MultiSelectField(max_length=5, choices=OTHER_WORK, blank=True)


class Person(BioData):
    bio_data = models.OneToOneField(BioData, on_delete=models.CASCADE, primary_key=True)
    specialization = models.OneToOneField(Specialization, on_delete=models.CASCADE, null=True)
    spiritual_data = models.OneToOneField(SpiritualData, on_delete=models.CASCADE, null=True)
    church_work_history = models.OneToOneField(ChurchWorkHistory, on_delete=models.CASCADE, null=True)
