# Generated by Django 4.2.5 on 2023-09-14 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0006_whychooseusmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpcommingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upcomming_image', models.ImageField(upload_to='', verbose_name='static/uploads')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.categorymodel')),
            ],
        ),
    ]
