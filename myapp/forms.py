from django import forms
from .models import Contact, Apply

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        labels = {
            'name': 'Your Name',
            'email': 'Your Email',
            'message': 'Message',
        }

class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = '__all__'
        labels = {
            'area_of_service': 'Which area of service',
            'enterprise_name': 'Name of enterprise',
            'primary_contact_person': 'Primary contact person',
            'primary_contact_email': 'Email address',
            'contact_number': 'Contact number',
            'enterprise_address': 'Enterprise name and address',
            'primary_representative': 'Primary representative',
            'num_employees_contributing_to_uif': 'Total number of employees contributing to UIF',
            'uif_number': 'UIF number',
            'tax_clearance_certificate': 'Tax clearance certificate',
            'enterprise_registration_number': 'Enterprise registration number',
            'audited_statements': '24 Months audited statements (yes/no)',
            'accounting_firm_or_accountant_name': 'Name of accounting firm and/or accountant',
            'management_accounts_and_cash_flow_projections': 'Management accounts and cash flow projections (yes/no)',
            'field_of_operation': 'Field of operation',
            'years_in_operation': 'Years in operation',
            'future_orders_or_new_business_areas': 'Any future orders or new business areas',
            'agreement': 'I agree to the terms',
        }
