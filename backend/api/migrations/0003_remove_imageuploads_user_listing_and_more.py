# Generated by Django 5.0.6 on 2024-06-09 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_multiimagepost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageuploads',
            name='user_listing',
        ),
        migrations.DeleteModel(
            name='PropertyImage',
        ),
        migrations.RemoveField(
            model_name='userlisting',
            name='user',
        ),
        migrations.DeleteModel(
            name='ImageUploads',
        ),
        migrations.DeleteModel(
            name='UserListing',
        ),
    ]
