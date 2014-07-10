# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.aggregates import Count
from django.utils.translation import ugettext_lazy as _
from polymorphic.manager import PolymorphicManager
from polymorphic.polymorphic_model import PolymorphicModel
from shop.util.fields import CurrencyField
from .order import BaseOrderItem


class ProductManager(PolymorphicManager):
    """
    A more classic manager for Product filtering and manipulation.
    """
    def active(self):
        return self.filter(active=True)


class ProductStatisticsManager(PolymorphicManager):
    """
    A Manager for all the non-object manipulation needs, mostly statistics and
    other "data-mining" toys.
    """

    def top_selling_products(self, quantity):
        """
        This method "mines" the previously passed orders, and gets a list of
        products (of a size equal to the quantity parameter), ordered by how
        many times they have been purchased.
        """
        OrderItem = getattr(BaseOrderItem, 'materialized_model')

        # Get an aggregate of product references and their respective counts
        top_products_data = OrderItem.objects.values('product') \
            .annotate(product_count=Count('product')) \
            .order_by('product_count')[:quantity]

        # The top_products_data result should be in the form:
        # [{'product_reference': '<product_id>', 'product_count': <count>}, ..]

        top_products_list = []  # The actual list of products
        for values in top_products_data:
            prod = values.get('product')
            # We could eventually return the count easily here, if needed.
            top_products_list.append(prod)

        return top_products_list


class BaseProduct(PolymorphicModel):
    """
    A basic product for the shop.

    Most of the already existing fields here should be generic enough to reside
    on the "base model" and not on an added property.
    """
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    slug = models.SlugField(verbose_name=_('Slug'), unique=True)
    active = models.BooleanField(default=False, verbose_name=_('Active'))
    date_added = models.DateTimeField(auto_now_add=True,
        verbose_name=_('Date added'))
    last_modified = models.DateTimeField(auto_now=True,
        verbose_name=_('Last modified'))
    unit_price = CurrencyField(verbose_name=_('Unit price'))
    objects = ProductManager()

    class Meta:
        abstract = True
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])

    def get_price(self):
        """
        Returns the price for this item (provided for extensibility).
        """
        return self.unit_price

    def get_name(self):
        """
        Returns the name of this Product (provided for extensibility).
        """
        return self.name

    def get_product_reference(self):
        """
        Returns product reference of this Product (provided for extensibility).
        """
        return unicode(self.pk)

    @property
    def can_be_added_to_cart(self):
        return self.active
