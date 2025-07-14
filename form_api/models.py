from django.db import models

# Create your models here.

class wheelSpecsForm(models.Model):
    form_number = models.CharField(max_length=100, unique=True)
    submitted_by = models.CharField(max_length=100)
    submitted_date = models.DateField()
    status = models.CharField(max_length=50, default="saved")

    #fields
    tread_diameter_new = models.CharField(max_length=100, blank=True, null=True)
    last_shop_issue_size = models.CharField(max_length=100, blank=True, null=True)
    condemning_dia = models.CharField(max_length=100, blank=True, null=True)
    wheel_gauge = models.CharField(max_length=100, blank=True, null=True)
    variation_same_axle = models.CharField(max_length=100, blank=True, null=True)
    variation_same_bogie = models.CharField(max_length=100, blank=True, null=True)
    variation_same_coach = models.CharField(max_length=100, blank=True, null=True)
    wheel_profile = models.CharField(max_length=100, blank=True, null=True)
    intermediate_wwp = models.CharField(max_length=100, blank=True, null=True)
    bearing_seat_diameter = models.CharField(max_length=100, blank=True, null=True)
    roller_bearing_outer_dia = models.CharField(max_length=100, blank=True, null=True)
    roller_bearing_bore_dia = models.CharField(max_length=100, blank=True, null=True)
    roller_bearing_width = models.CharField(max_length=100, blank=True, null=True)
    axle_box_housing_bore_dia = models.CharField(max_length=100, blank=True, null=True)
    wheel_disc_width = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.form_number