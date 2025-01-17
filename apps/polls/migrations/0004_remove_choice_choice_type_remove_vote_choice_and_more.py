# Generated by Django 4.2.11 on 2024-04-10 06:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0003_remove_choice_choice1_remove_choice_choice2_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="choice",
            name="choice_type",
        ),
        migrations.RemoveField(
            model_name="vote",
            name="choice",
        ),
        migrations.AddField(
            model_name="choice",
            name="choice1",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.AddField(
            model_name="choice",
            name="choice2",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.AddField(
            model_name="choice",
            name="choice3",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.AddField(
            model_name="choice",
            name="choice4",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.AddField(
            model_name="vote",
            name="choice_type",
            field=models.CharField(
                choices=[
                    ("CHOICE1", "Choice1"),
                    ("CHOICE2", "Choice2"),
                    ("CHOICE3", "Choice3"),
                    ("CHOICE4", "Choice4"),
                ],
                default="",
                max_length=15,
            ),
        ),
    ]
