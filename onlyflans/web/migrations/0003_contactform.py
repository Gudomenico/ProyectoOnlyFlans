# Generated by Django 5.1.2 on 2024-10-31 00:43

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_flan_descripcion_flan_img_url_flan_is_private_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_form_uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('customer_email', models.EmailField(default='', max_length=254)),
                ('customer_name', models.CharField(max_length=64)),
                ('message', models.TextField(default='')),
            ],
        ),
    ]