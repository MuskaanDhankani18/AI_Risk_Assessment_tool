from django.db import models

class Risk_Assessment(models.Model):
    business_name = models.CharField(max_length=255)
    industry = models.CharField(max_length=100)
    revenue = models.PositiveIntegerField(default=10)
    employees = models.PositiveIntegerField(default=10)
    location = models.CharField(max_length=255, default="unknown")
    financial_stability = models.FloatField()
    market_risk = models.FloatField()
    operational_risk = models.FloatField()
    compliance_risk = models.FloatField()
    cybersecurity_risk = models.FloatField(default=0.5)
    risk_score = models.FloatField(null=True, blank=True)  

    def __str__(self):
        return self.business_name
