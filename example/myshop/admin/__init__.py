# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib import admin

from shop.admin.defaults import customer
from shop.admin.defaults.order import OrderAdmin
from shop.models.defaults.order import Order
from shop.admin.order import PrintOrderAdminMixin


# models defined by the myshop instance itself
if settings.SHOP_TUTORIAL in ['commodity', 'i18n_commodity']:
    from shop.admin.defaults import commodity

else:
    from . import manufacturer

if settings.SHOP_PARTIAL_DELIVERY:
    from shop.admin.delivery import DeliveryOrderAdminMixin

    class OrderAdmin(PrintOrderAdminMixin, DeliveryOrderAdminMixin, OrderAdmin):
        pass
else:
    class OrderAdmin(PrintOrderAdminMixin, OrderAdmin):
        pass

if 'shop_sendcloud' in settings.INSTALLED_APPS:
    from shop_sendcloud.admin import SendCloudOrderAdminMixin

    class OrderAdmin(SendCloudOrderAdminMixin, OrderAdmin):
        pass

admin.site.register(Order, OrderAdmin)

if settings.SHOP_TUTORIAL == 'smartcard':
    from . import smartcard

elif settings.SHOP_TUTORIAL == 'i18n_smartcard':
    from . import i18n_smartcard

elif settings.SHOP_TUTORIAL == 'polymorphic':
    from . import polymorphic_

elif settings.SHOP_TUTORIAL == 'i18n_polymorphic':
    from . import i18n_polymorphic


__all__ = ['commodity', 'customer']

admin.site.site_header = "Django-SHOP administration"
