from django.contrib import admin
from .models import Flan, ContactForm, Locales

@admin.register(Flan)
class FlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_private')  
    search_fields = ('name',)  
    
@admin.register(ContactForm)  
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_email', 'contact_form_uuid')  
    search_fields = ('customer_name', 'customer_email') 
    
@admin.register(Locales)
class LocalesAdmin(admin.ModelAdmin):
    list_display= ('name', 'in_earth')
    search_fields = ('name',)  