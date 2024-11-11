from django.db import models
import uuid

# Create your models here.

class Flan (models.Model):
    name = models.CharField(max_length = 64)
    descripcion = models.TextField(default="")
    img_url = models.URLField(default="")
    slug= models.SlugField(default="default-slug")
    is_private= models.BooleanField(default=False)
    
#flan_uuid = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
#Se me olvido agregarlo :(. Voy a dejar que django gestione la primary key con "id".
    
class ContactForm (models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email= models.EmailField(default="")
    customer_name = models.CharField(max_length = 64)
    message = models.TextField(default="")
    
    def __str__(self):
        return f"Contact form from {self.customer_name} ({self.customer_email})"
    
class Locales (models.Model):
    name = models.CharField(max_length = 64)
    descripcion = models.TextField(default="")
    img = models.URLField(default="")
    in_earth= models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

