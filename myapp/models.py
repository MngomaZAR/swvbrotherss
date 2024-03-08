from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Apply(models.Model):
    area_of_service_choices = [
        ('construction', 'Construction'),
        ('logistics', 'Logistics'),
        ('grantfunding', 'Grant Funding for Distressed Enterprises'),
    ]
    area_of_service = models.CharField(max_length=50, choices=area_of_service_choices, blank=True, null=True)
    enterprise_name = models.CharField(max_length=100, blank=True, null=True)
    primary_contact_person = models.CharField(max_length=100, blank=True, null=True)
    primary_contact_email = models.EmailField(blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    enterprise_address = models.TextField(blank=True, null=True)
    primary_representative = models.CharField(max_length=100, blank=True, null=True)
    num_employees_contributing_to_uif = models.IntegerField(blank=True, null=True)
    uif_number = models.CharField(max_length=100, blank=True, null=True)
    tax_clearance_certificate = models.BooleanField(default=False)
    enterprise_registration_number = models.CharField(max_length=100, blank=True, null=True)
    audited_statements = models.BooleanField(default=False)
    accounting_firm_or_accountant_name = models.CharField(max_length=100, blank=True, null=True)
    management_accounts_and_cash_flow_projections = models.BooleanField(default=False)
    field_of_operation = models.CharField(max_length=100, blank=True, null=True)
    years_in_operation = models.IntegerField(blank=True, null=True)
    future_orders_or_new_business_areas = models.TextField(blank=True, null=True)
    agreement = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.enterprise_name} - {self.primary_contact_person}"
