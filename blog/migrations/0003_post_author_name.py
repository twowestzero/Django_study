# Generated by Django 2.1.5 on 2019-01-19 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author_name',
            field=models.CharField(default='anonymous', max_length=20),
            preserve_default=False,
        ),
    ]
