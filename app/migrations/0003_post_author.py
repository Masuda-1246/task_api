# Generated by Django 4.0.1 on 2022-06-11 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_post_lang_post_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.TextField(default=1, verbose_name='author'),
            preserve_default=False,
        ),
    ]