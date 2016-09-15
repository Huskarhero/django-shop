# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-02 11:37
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField("ShippingAddress", "addressee", "name"),
        migrations.RenameField("ShippingAddress", "street", "address1"),
        migrations.RenameField("ShippingAddress", "supplement", "address2"),
        migrations.RenameField("ShippingAddress", "location", "city"),

        migrations.AlterField("ShippingAddress", "name", models.CharField(
            verbose_name="Full name", max_length=1024
        )),
        migrations.AlterField("ShippingAddress", "address1", models.CharField(
            verbose_name="Address line 1", max_length=1024
        )),
        migrations.AlterField("ShippingAddress", "address2", models.CharField(
            verbose_name="Address line 2", max_length=1024
        )),
        migrations.AlterField("ShippingAddress", "city", models.CharField(
            verbose_name="City", max_length=1024
        )),

        migrations.RenameField("BillingAddress", "addressee", "name"),
        migrations.RenameField("BillingAddress", "street", "address1"),
        migrations.RenameField("BillingAddress", "supplement", "address2"),
        migrations.RenameField("BillingAddress", "location", "city"),

        migrations.AlterField("BillingAddress", "name", models.CharField(
            verbose_name="Full name", max_length=1024
        )),
        migrations.AlterField("BillingAddress", "address1", models.CharField(
            verbose_name="Address line 1", max_length=1024
        )),
        migrations.AlterField("BillingAddress", "address2", models.CharField(
            verbose_name="Address line 2", max_length=1024
        )),
        migrations.AlterField("BillingAddress", "city", models.CharField(
            verbose_name="City", max_length=1024
        )),
    ]
