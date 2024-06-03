from django.db import models

# Create your models here.


class line(models.Model):
    line_name = models.CharField(max_length=255)
    target = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.line_name

class operator(models.Model):
    name = models.CharField(max_length=255)
    line = models.ForeignKey(line, on_delete=models.CASCADE)
    employee_code = models.CharField(max_length=255, blank=True, null=True)
    daily_target = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class daily_report(models.Model):
    operator_name = models.ForeignKey(operator, on_delete=models.CASCADE)
    line = models.ForeignKey(line, on_delete=models.CASCADE)
    h1 = models.PositiveIntegerField(default=0)
    h2 = models.PositiveIntegerField(default=0)
    h3 = models.PositiveIntegerField(default=0)
    h4 = models.PositiveIntegerField(default=0)
    h5 = models.PositiveIntegerField(default=0)
    h6 = models.PositiveIntegerField(default=0)
    h7 = models.PositiveIntegerField(default=0)
    h8 = models.PositiveIntegerField(default=0)
    h9 = models.PositiveIntegerField(default=0)
    h10 = models.PositiveIntegerField(default=0)
    h11 = models.PositiveIntegerField(default=0)
    h12 = models.PositiveIntegerField(default=0)
    target_qty = models.PositiveIntegerField(default=0)
    target_per = models.PositiveIntegerField(default=0)
    created_date = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.operator_name
    
