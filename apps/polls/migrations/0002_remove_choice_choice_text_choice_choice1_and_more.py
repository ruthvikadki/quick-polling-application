# Generated by Django 4.2.11 on 2024-04-10 06:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="choice",
            name="choice_text",
        ),
        migrations.AddField(
            model_name="choice",
            name="choice1",
            field=models.CharField(default=True, max_length=200),
        ),
        migrations.AddField(
            model_name="choice",
            name="choice2",
            field=models.CharField(default=True, max_length=200),
        ),
        migrations.AddField(
            model_name="choice",
            name="choice3",
            field=models.CharField(default=True, max_length=200),
        ),
        migrations.AddField(
            model_name="choice",
            name="choice4",
            field=models.CharField(default=True, max_length=200),
        ),
    ]
