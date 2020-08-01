# Generated by Django 3.0.8 on 2020-07-27 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=36)),
                ('user_username', models.CharField(max_length=36)),
                ('user_password', models.CharField(max_length=36)),
                ('user_confirm_password', models.CharField(max_length=36)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_contact', models.IntegerField()),
                ('gender', models.IntegerField(choices=[(0, 'Male'), (1, 'Female')])),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.Area')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.City')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.Country')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.State')),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('messages_id', models.AutoField(primary_key=True, serialize=False)),
                ('messages_text', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.User')),
            ],
        ),
        migrations.CreateModel(
            name='IdProof',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.ImageField(upload_to='idproof/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.User')),
            ],
        ),
    ]
