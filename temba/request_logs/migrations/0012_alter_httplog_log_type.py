# Generated by Django 3.2.7 on 2021-09-24 13:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("request_logs", "0011_httplog_num_retries"),
    ]

    operations = [
        migrations.AlterField(
            model_name="httplog",
            name="log_type",
            field=models.CharField(
                choices=[
                    ("webhook_called", "Webhook Called"),
                    ("intents_synced", "Intents Synced"),
                    ("classifier_called", "Classifier Called"),
                    ("ticketer_called", "Ticketing Service Called"),
                    ("airtime_transferred", "Airtime Transferred"),
                    ("whatsapp_templates_synced", "WhatsApp Templates Synced"),
                    ("whatsapp_tokens_synced", "WhatsApp Tokens Synced"),
                    ("whatsapp_contacts_refreshed", "WhatsApp Contacts Refreshed"),
                    ("whataspp_check_health", "WhatsApp Health Check"),
                ],
                max_length=32,
            ),
        ),
    ]
