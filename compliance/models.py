from django.db import models
from django.forms import ModelForm

# Create your models here.

"""class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)"""


class Branches(models.Model):
    branch_code = models.CharField(max_length=5)
    branch_name = models.CharField(max_length=30)
    branch_address = models.CharField(max_length=100)
    opening_date = models.DateField('Date of Branch Open')

class Inspections(models.Model):
    COMPREHENSIVE = 'CM'
    SPECIAL = 'SP'
    #JUNIOR = 'JR'
    #SENIOR = 'SR'
    INSPECTION_CHOICES = (
        (COMPREHENSIVE, 'Comprehensive Inspection'),
        (SPECIAL, 'Special Inspection'),
        #(JUNIOR, 'Junior'),
        #(SENIOR, 'Senior'),
    )
    branch_id = models.ForeignKey(Branches,on_delete=models.CASCADE)
    base_date = models.DateField('base date of the audit')
    start_date = models.DateField('Starting day of the inspection')
    end_date = models.DateField('Ending day of the inspection')
    #submission_date = models.DateField('Report submission date')
    inspection_type = models.CharField(max_length=2,
                                      choices=INSPECTION_CHOICES,
                                      default=COMPREHENSIVE)


class Compliances(models.Model):
        inspection_id = models.ForeignKey(Inspections,on_delete=models.CASCADE)
        compliance_number = models.PositiveIntegerField('Number of Compliance')
        #findings_number = models.PositiveIntegerField('Number of Findings')
        #rectified_number = models.PositiveIntegerField('Number of Findings rectified')
        gb_rect = models.PositiveIntegerField('Number of findings rectified - GB',default=0)
        cr_rect = models.PositiveIntegerField('Number of findings rectified - CR',default=0)
        fx_rect = models.PositiveIntegerField('Number of findings rectified - FX',default=0)
        ict_rect = models.PositiveIntegerField('Number of findings rectified - ICT',default=0)
        compliance_date = models.DateField('Compliance date')

class Reports(models.Model):
    inspection_id = models.ForeignKey(Inspections,on_delete=models.CASCADE)
    submission_date = models.DateField('Report submission date')
    gb_finding = models.PositiveIntegerField('Number of Findings in GB',default=0)
    cr_finding = models.PositiveIntegerField('Number of Findings in Credit',default=0)
    fx_finding = models.PositiveIntegerField('Number of Findings in Froeign Exchange',default=0)
    ict_finding = models.PositiveIntegerField('Number of Findings in ICT',default=0)
