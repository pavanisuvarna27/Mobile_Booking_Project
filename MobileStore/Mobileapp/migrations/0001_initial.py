# Generated by Django 3.0.6 on 2021-01-07 06:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(default=18)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=7)),
                ('image', models.ImageField(default='user.jpg', upload_to='Profile_pics/')),
                ('p', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('description', models.TextField(default='', max_length=200)),
                ('image', models.ImageField(upload_to='products/')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Mobileapp.category')),
            ],
        ),
    ]
