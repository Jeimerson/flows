# Generated by Django 2.2.10 on 2020-12-04 17:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("contacts", "0128_squashed"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("campaigns", "0035_squashed"),
    ]

    operations = [
        migrations.AddField(
            model_name="eventfire",
            name="contact",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="campaign_fires", to="contacts.Contact"
            ),
        ),
        migrations.AddField(
            model_name="eventfire",
            name="event",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="fires", to="campaigns.CampaignEvent"
            ),
        ),
        migrations.AddField(
            model_name="campaignevent",
            name="campaign",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="events", to="campaigns.Campaign"
            ),
        ),
        migrations.AddField(
            model_name="campaignevent",
            name="created_by",
            field=models.ForeignKey(
                help_text="The user which originally created this item",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="campaigns_campaignevent_creations",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
