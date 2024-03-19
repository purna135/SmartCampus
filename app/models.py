from django.db import models

# Create your models here.
class IrrigationData(models.Model):
    id = models.AutoField(primary_key=True)
    pump_status = models.BooleanField(default=False, blank=True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    ph_level = models.DecimalField(default=0.0, max_digits=5, decimal_places=2)
    moisture_level = models.DecimalField(default=0.0, max_digits=5, decimal_places=2)
    soil_temperature = models.DecimalField(default=0.0, max_digits=5, decimal_places=2)
    nitrogen = models.DecimalField(default=0.0, max_digits=5, decimal_places=2, verbose_name='Nitrogen (N)')
    phosphorus = models.DecimalField(default=0.0, max_digits=5, decimal_places=2, verbose_name='Phosphorus (P)')
    potassium = models.DecimalField(default=0.0, max_digits=5, decimal_places=2, verbose_name='Potassium (K)')

    def __str__(self):
        return f"Irrigation Data for {self.date} {self.time}"
