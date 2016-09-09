# -*- coding: utf-8
from __future__ import unicode_literals

from django.test import TestCase

from shop.models.defaults.customer import Customer


class JSONFieldTest(TestCase):
    """JSONField Wrapper Tests"""

    def test_json_field_create(self):
        """Test saving a JSON object in our JSONField"""
        json_obj = {
            "item_1": "this is a json blah",
            "blergh": "hey, hey, hey"}

        obj = Customer.objects.create(extra=json_obj)
        new_obj = Customer.objects.get(id=obj.id)

        self.assertEqual(new_obj.extra, json_obj)
