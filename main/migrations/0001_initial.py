# Generated by Django 5.0.7 on 2024-07-23 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tutorial",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tutorial_title", models.CharField(max_length=200)),
                ("tutorial_content", models.TextField()),
                (
                    "tutorial_published",
                    models.DateTimeField(verbose_name="date published"),
                ),
            ],
        ),
    ]
