# Generated by Django 4.1.7 on 2023-03-28 08:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ideas', '0005_rename_about_contributing_ideasmodel_about_contributor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ideasmodel',
            name='user',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, related_name='Contributor_post', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
