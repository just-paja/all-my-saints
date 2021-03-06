# Generated by Django 3.2.7 on 2021-09-06 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compro', '0006_auto_20210905_1218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documentation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField(null=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='documentation_items', to='compro.team')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DocumentationMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='documentation/photos')),
                ('video', models.FileField(upload_to='documentation/videos')),
                ('documentation', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='media', to='compro.documentation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='compromedia',
            name='compro',
        ),
        migrations.DeleteModel(
            name='Compro',
        ),
        migrations.DeleteModel(
            name='ComproMedia',
        ),
    ]
