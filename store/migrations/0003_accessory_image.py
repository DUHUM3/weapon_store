# Generated by Django 5.1 on 2024-10-02 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_accessory'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessory',
            name='image',
            field=models.ImageField(default='accessories/default.jpg', upload_to='accessories/'),
        ),
    ]
