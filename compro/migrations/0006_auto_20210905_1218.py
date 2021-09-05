# Generated by Django 3.2.7 on 2021-09-05 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compro', '0005_hollycompro_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='hollycompro',
            name='slug',
            field=models.SlugField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hollycompro',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=9, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='hollycompro',
            name='lng',
            field=models.DecimalField(blank=True, decimal_places=9, max_digits=12, null=True),
        ),
    ]
