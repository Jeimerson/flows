# Generated by Django 2.1.8 on 2019-07-01 20:55

import uuid

import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

import temba.utils.json
import temba.utils.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("csv_imports", "0004_auto_20170223_0917"),
        ("orgs", "0055_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "is_active",
                    models.BooleanField(
                        default=True, help_text="Whether this item is active, use this instead of deleting"
                    ),
                ),
                (
                    "created_on",
                    models.DateTimeField(
                        blank=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        help_text="When this item was originally created",
                    ),
                ),
                (
                    "modified_on",
                    models.DateTimeField(
                        blank=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        help_text="When this item was last modified",
                    ),
                ),
                (
                    "uuid",
                    models.CharField(
                        db_index=True,
                        default=temba.utils.models.generate_uuid,
                        help_text="The unique identifier for this object",
                        max_length=36,
                        unique=True,
                        verbose_name="Unique Identifier",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True,
                        help_text="The name of this contact",
                        max_length=128,
                        null=True,
                        verbose_name="Name",
                    ),
                ),
                (
                    "language",
                    models.CharField(
                        blank=True,
                        help_text="The preferred language for this contact",
                        max_length=3,
                        null=True,
                        verbose_name="Language",
                    ),
                ),
                ("is_blocked", models.BooleanField(default=False)),
                ("is_stopped", models.BooleanField(default=False)),
                ("fields", temba.utils.models.JSONField(encoder=temba.utils.json.TembaEncoder, null=True)),
                ("is_test", models.BooleanField(default=False, null=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="contacts_contact_creations",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="contacts_contact_modifications",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "org",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, related_name="contacts", to="orgs.Org"
                    ),
                ),
            ],
            options={"abstract": False},
            bases=(temba.utils.models.RequireUpdateFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name="ContactField",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "is_active",
                    models.BooleanField(
                        default=True, help_text="Whether this item is active, use this instead of deleting"
                    ),
                ),
                (
                    "created_on",
                    models.DateTimeField(
                        blank=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        help_text="When this item was originally created",
                    ),
                ),
                (
                    "modified_on",
                    models.DateTimeField(
                        blank=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        help_text="When this item was last modified",
                    ),
                ),
                ("uuid", models.UUIDField(default=uuid.uuid4, unique=True)),
                ("label", models.CharField(max_length=36, verbose_name="Label")),
                ("key", models.CharField(max_length=36, verbose_name="Key")),
                (
                    "value_type",
                    models.CharField(
                        choices=[
                            ("T", "Text"),
                            ("N", "Number"),
                            ("D", "Date & Time"),
                            ("S", "State"),
                            ("I", "District"),
                            ("W", "Ward"),
                        ],
                        default="T",
                        max_length=1,
                        verbose_name="Field Type",
                    ),
                ),
                (
                    "show_in_table",
                    models.BooleanField(default=False, help_text="Featured field", verbose_name="Shown in Tables"),
                ),
                ("priority", models.PositiveIntegerField(default=0)),
                ("field_type", models.CharField(choices=[("S", "System"), ("U", "User")], default="U", max_length=1)),
                (
                    "created_by",
                    models.ForeignKey(
                        help_text="The user which originally created this item",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="contacts_contactfield_creations",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        help_text="The user which last modified this item",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="contacts_contactfield_modifications",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "org",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="contactfields",
                        to="orgs.Org",
                        verbose_name="Org",
                    ),
                ),
            ],
            options={"abstract": False},
            managers=[("all_fields", django.db.models.manager.Manager())],
        ),
        migrations.CreateModel(
            name="ContactGroup",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "is_active",
                    models.BooleanField(
                        default=True, help_text="Whether this item is active, use this instead of deleting"
                    ),
                ),
                (
                    "created_on",
                    models.DateTimeField(
                        blank=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        help_text="When this item was originally created",
                    ),
                ),
                (
                    "modified_on",
                    models.DateTimeField(
                        blank=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        help_text="When this item was last modified",
                    ),
                ),
                (
                    "uuid",
                    models.CharField(
                        db_index=True,
                        default=temba.utils.models.generate_uuid,
                        help_text="The unique identifier for this object",
                        max_length=36,
                        unique=True,
                        verbose_name="Unique Identifier",
                    ),
                ),
                (
                    "name",
                    models.CharField(help_text="The name of this contact group", max_length=64, verbose_name="Name"),
                ),
                (
                    "group_type",
                    models.CharField(
                        choices=[
                            ("A", "All Contacts"),
                            ("B", "Blocked Contacts"),
                            ("S", "Stopped Contacts"),
                            ("U", "User Defined Groups"),
                        ],
                        default="U",
                        help_text="What type of group it is, either user defined or one of our system groups",
                        max_length=1,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("I", "Initializing"), ("V", "Evaluating"), ("R", "Ready")], default="I", max_length=1
                    ),
                ),
                ("query", models.TextField(help_text="The membership query for this group", null=True)),
                (
                    "contacts",
                    models.ManyToManyField(related_name="all_groups", to="contacts.Contact", verbose_name="Contacts"),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        help_text="The user which originally created this item",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="contacts_contactgroup_creations",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "import_task",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to="csv_imports.ImportTask"
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        help_text="The user which last modified this item",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="contacts_contactgroup_modifications",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "org",
                    models.ForeignKey(
                        help_text="The organization this group is part of",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="all_groups",
                        to="orgs.Org",
                        verbose_name="Org",
                    ),
                ),
                ("query_fields", models.ManyToManyField(to="contacts.ContactField", verbose_name="Query Fields")),
            ],
            options={"abstract": False},
            managers=[("all_groups", django.db.models.manager.Manager())],
        ),
        migrations.CreateModel(
            name="ContactGroupCount",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "is_squashed",
                    models.BooleanField(default=False, help_text="Whether this row was created by squashing"),
                ),
                ("count", models.IntegerField(default=0)),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, related_name="counts", to="contacts.ContactGroup"
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="ContactURN",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "identity",
                    models.CharField(
                        help_text="The Universal Resource Name as a string, excluding display if present. ex: tel:+250788383383",
                        max_length=255,
                    ),
                ),
                (
                    "path",
                    models.CharField(help_text="The path component of our URN. ex: +250788383383", max_length=255),
                ),
                (
                    "display",
                    models.CharField(
                        help_text="The display component for this URN, if any", max_length=255, null=True
                    ),
                ),
                (
                    "scheme",
                    models.CharField(
                        help_text="The scheme for this URN, broken out for optimization reasons, ex: tel",
                        max_length=128,
                    ),
                ),
                (
                    "priority",
                    models.IntegerField(
                        default=50, help_text="The priority of this URN for the contact it is associated with"
                    ),
                ),
                ("auth", models.TextField(help_text="Any authentication information needed by this URN", null=True)),
                (
                    "contact",
                    models.ForeignKey(
                        blank=True,
                        help_text="The contact that this URN is for, can be null",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="urns",
                        to="contacts.Contact",
                    ),
                ),
                (
                    "org",
                    models.ForeignKey(
                        help_text="The organization for this URN, can be null",
                        on_delete=django.db.models.deletion.PROTECT,
                        to="orgs.Org",
                    ),
                ),
            ],
            options={"ordering": ("-priority", "id")},
        ),
        migrations.CreateModel(
            name="ExportContactsTask",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "is_active",
                    models.BooleanField(
                        default=True, help_text="Whether this item is active, use this instead of deleting"
                    ),
                ),
                (
                    "created_on",
                    models.DateTimeField(
                        blank=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        help_text="When this item was originally created",
                    ),
                ),
                (
                    "modified_on",
                    models.DateTimeField(
                        blank=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        help_text="When this item was last modified",
                    ),
                ),
                (
                    "uuid",
                    models.CharField(
                        db_index=True,
                        default=temba.utils.models.generate_uuid,
                        help_text="The unique identifier for this object",
                        max_length=36,
                        unique=True,
                        verbose_name="Unique Identifier",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("P", "Pending"), ("O", "Processing"), ("C", "Complete"), ("F", "Failed")],
                        default="P",
                        max_length=1,
                    ),
                ),
                ("search", models.TextField(blank=True, help_text="The search query", null=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        help_text="The user which originally created this item",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="contacts_exportcontactstask_creations",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        help_text="The unique group to export",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="exports",
                        to="contacts.ContactGroup",
                    ),
                ),
                ("group_memberships", models.ManyToManyField(to="contacts.ContactGroup")),
                (
                    "modified_by",
                    models.ForeignKey(
                        help_text="The user which last modified this item",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="contacts_exportcontactstask_modifications",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "org",
                    models.ForeignKey(
                        help_text="The organization of the user.",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="exportcontactstasks",
                        to="orgs.Org",
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.AlterUniqueTogether(name="contacturn", unique_together={("identity", "org")}),
    ]
