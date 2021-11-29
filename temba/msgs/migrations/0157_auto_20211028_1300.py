# Generated by Django 3.2.8 on 2021-10-28 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("msgs", "0156_auto_20210722_1429"),
    ]

    operations = [
        migrations.AlterField(
            model_name="broadcast",
            name="status",
            field=models.CharField(
                choices=[("I", "Initializing"), ("Q", "Queued"), ("S", "Sent"), ("F", "Failed")],
                default="I",
                max_length=1,
            ),
        ),
        migrations.AlterField(
            model_name="msg",
            name="status",
            field=models.CharField(
                choices=[
                    ("I", "Initializing"),
                    ("P", "Pending"),
                    ("Q", "Queued"),
                    ("W", "Wired"),
                    ("S", "Sent"),
                    ("D", "Delivered"),
                    ("H", "Handled"),
                    ("E", "Error"),
                    ("F", "Failed"),
                    ("R", "Resent"),
                ],
                db_index=True,
                default="P",
                max_length=1,
            ),
        ),
    ]
