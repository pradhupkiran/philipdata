# Generated by Django 4.2.13 on 2024-06-07 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='address',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='detail',
            name='address2',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='detail',
            name='city',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='detail',
            name='contact_person',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='detail',
            name='country',
            field=models.CharField(blank=True, max_length=75, null=True),
        ),
        migrations.AlterField(
            model_name='detail',
            name='email_id',
            field=models.EmailField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='detail',
            name='email_id_2',
            field=models.EmailField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='detail',
            name='name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='detail',
            name='technology',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='detail',
            name='technology_2',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='detail',
            name='technology_3',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='detail',
            name='tel_no',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='detail',
            name='town',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='detail',
            name='website',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
