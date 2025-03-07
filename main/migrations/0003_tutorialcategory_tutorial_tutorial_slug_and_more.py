# Generated by Django 5.0.7 on 2024-07-26 08:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_alter_tutorial_tutorial_published"),
    ]

    operations = [
        migrations.CreateModel(
            name="TutorialCategory",
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
                ("tutorial_category", models.CharField(max_length=200)),
                ("category_summary", models.CharField(max_length=200)),
                ("category_slug", models.CharField(max_length=200)),
            ],
            options={
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.AddField(
            model_name="tutorial",
            name="tutorial_slug",
            field=models.CharField(default=1, max_length=200),
        ),
        migrations.CreateModel(
            name="TutorialSeries",
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
                ("tutorial_series", models.CharField(max_length=200)),
                ("series_summary", models.CharField(max_length=200)),
                (
                    "tutorial_category",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to="main.tutorialcategory",
                        verbose_name="Category",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Series",
            },
        ),
        migrations.AddField(
            model_name="tutorial",
            name="tutorial_series",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                to="main.tutorialseries",
                verbose_name="Series",
            ),
        ),
    ]
