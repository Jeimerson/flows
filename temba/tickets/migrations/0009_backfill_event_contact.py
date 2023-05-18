# Generated by Django 2.2.20 on 2021-06-17 21:14

from django.db import migrations


def backfill_event_contact(apps, schema_editor):  # pragma: no cover
    TicketEvent = apps.get_model("tickets", "TicketEvent")
    for event in TicketEvent.objects.select_related("ticket__contact"):
        event.contact = event.ticket.contact
        event.save(update_fields=("contact",))


class Migration(migrations.Migration):
    dependencies = [
        ("tickets", "0008_auto_20210617_1425"),
    ]

    operations = [migrations.RunPython(backfill_event_contact)]
