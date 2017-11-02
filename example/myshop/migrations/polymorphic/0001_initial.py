# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-22 22:12
from __future__ import unicode_literals

import cms.models.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone
import django_fsm
import djangocms_text_ckeditor.fields
import filer.fields.image
import shop.models.address
import shop.models.fields
import shop.models.product
import shop.money.fields
import shop.payment.defaults
import shop.shipping.delivery
import shop_stripe.payment


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('filer', '0007_auto_20161016_1055'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('email_auth', '0003_django110'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.SmallIntegerField(db_index=True, default=0, help_text='Priority for using this address')),
                ('name', models.CharField(max_length=1024, verbose_name='Full name')),
                ('address1', models.CharField(max_length=1024, verbose_name='Address line 1')),
                ('address2', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Address line 2')),
                ('zip_code', models.CharField(max_length=12, verbose_name='ZIP / Postal code')),
                ('city', models.CharField(max_length=1024, verbose_name='City')),
                ('country', shop.models.address.CountryField(choices=[('AF', 'Afghanistan'), ('AX', 'Aland Islands'), ('AL', 'Albania'), ('DZ', 'Algeria'), ('AS', 'American Samoa'), ('AD', 'Andorra'), ('AO', 'Angola'), ('AI', 'Anguilla'), ('AQ', 'Antarctica'), ('AG', 'Antigua And Barbuda'), ('AR', 'Argentina'), ('AM', 'Armenia'), ('AW', 'Aruba'), ('AU', 'Australia'), ('AT', 'Austria'), ('AZ', 'Azerbaijan'), ('BS', 'Bahamas'), ('BH', 'Bahrain'), ('BD', 'Bangladesh'), ('BB', 'Barbados'), ('BY', 'Belarus'), ('BE', 'Belgium'), ('BZ', 'Belize'), ('BJ', 'Benin'), ('BM', 'Bermuda'), ('BT', 'Bhutan'), ('BO', 'Bolivia, Plurinational State Of'), ('BQ', 'Bonaire, Saint Eustatius And Saba'), ('BA', 'Bosnia And Herzegovina'), ('BW', 'Botswana'), ('BV', 'Bouvet Island'), ('BR', 'Brazil'), ('IO', 'British Indian Ocean Territory'), ('BN', 'Brunei Darussalam'), ('BG', 'Bulgaria'), ('BF', 'Burkina Faso'), ('BI', 'Burundi'), ('KH', 'Cambodia'), ('CM', 'Cameroon'), ('CA', 'Canada'), ('CV', 'Cape Verde'), ('KY', 'Cayman Islands'), ('CF', 'Central African Republic'), ('TD', 'Chad'), ('CL', 'Chile'), ('CN', 'China'), ('CX', 'Christmas Island'), ('CC', 'Cocos (Keeling) Islands'), ('CO', 'Colombia'), ('KM', 'Comoros'), ('CG', 'Congo'), ('CD', 'Congo, The Democratic Republic Of The'), ('CK', 'Cook Islands'), ('CR', 'Costa Rica'), ('HR', 'Croatia'), ('CU', 'Cuba'), ('CW', 'Curacao'), ('CY', 'Cyprus'), ('CZ', 'Czech Republic'), ('DK', 'Denmark'), ('DJ', 'Djibouti'), ('DM', 'Dominica'), ('DO', 'Dominican Republic'), ('EC', 'Ecuador'), ('EG', 'Egypt'), ('SV', 'El Salvador'), ('GQ', 'Equatorial Guinea'), ('ER', 'Eritrea'), ('EE', 'Estonia'), ('ET', 'Ethiopia'), ('FK', 'Falkland Islands (Malvinas)'), ('FO', 'Faroe Islands'), ('FJ', 'Fiji'), ('FI', 'Finland'), ('FR', 'France'), ('GF', 'French Guiana'), ('PF', 'French Polynesia'), ('TF', 'French Southern Territories'), ('GA', 'Gabon'), ('GM', 'Gambia'), ('DE', 'Germany'), ('GH', 'Ghana'), ('GI', 'Gibraltar'), ('GR', 'Greece'), ('GL', 'Greenland'), ('GD', 'Grenada'), ('GP', 'Guadeloupe'), ('GU', 'Guam'), ('GT', 'Guatemala'), ('GG', 'Guernsey'), ('GN', 'Guinea'), ('GW', 'Guinea-Bissau'), ('GY', 'Guyana'), ('HT', 'Haiti'), ('HM', 'Heard Island and McDonald Islands'), ('VA', 'Holy See (Vatican City State)'), ('HN', 'Honduras'), ('HK', 'Hong Kong'), ('HU', 'Hungary'), ('IS', 'Iceland'), ('IN', 'India'), ('ID', 'Indonesia'), ('IR', 'Iran, Islamic Republic Of'), ('IQ', 'Iraq'), ('IE', 'Ireland'), ('IL', 'Israel'), ('IT', 'Italy'), ('CI', 'Ivory Coast'), ('JM', 'Jamaica'), ('JP', 'Japan'), ('JE', 'Jersey'), ('JO', 'Jordan'), ('KZ', 'Kazakhstan'), ('KE', 'Kenya'), ('KI', 'Kiribati'), ('KP', "Korea, Democratic People's Republic Of"), ('KR', 'Korea, Republic Of'), ('KS', 'Kosovo'), ('KW', 'Kuwait'), ('KG', 'Kyrgyzstan'), ('LA', "Lao People's Democratic Republic"), ('LV', 'Latvia'), ('LB', 'Lebanon'), ('LS', 'Lesotho'), ('LR', 'Liberia'), ('LY', 'Libyan Arab Jamahiriya'), ('LI', 'Liechtenstein'), ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('MO', 'Macao'), ('MK', 'Macedonia'), ('MG', 'Madagascar'), ('MW', 'Malawi'), ('MY', 'Malaysia'), ('MV', 'Maldives'), ('ML', 'Mali'), ('ML', 'Malta'), ('MH', 'Marshall Islands'), ('MQ', 'Martinique'), ('MR', 'Mauritania'), ('MU', 'Mauritius'), ('YT', 'Mayotte'), ('MX', 'Mexico'), ('FM', 'Micronesia'), ('MD', 'Moldova'), ('MC', 'Monaco'), ('MN', 'Mongolia'), ('ME', 'Montenegro'), ('MS', 'Montserrat'), ('MA', 'Morocco'), ('MZ', 'Mozambique'), ('MM', 'Myanmar'), ('NA', 'Namibia'), ('NR', 'Nauru'), ('NP', 'Nepal'), ('NL', 'Netherlands'), ('AN', 'Netherlands Antilles'), ('NC', 'New Caledonia'), ('NZ', 'New Zealand'), ('NI', 'Nicaragua'), ('NE', 'Niger'), ('NG', 'Nigeria'), ('NU', 'Niue'), ('NF', 'Norfolk Island'), ('MP', 'Northern Mariana Islands'), ('NO', 'Norway'), ('OM', 'Oman'), ('PK', 'Pakistan'), ('PW', 'Palau'), ('PS', 'Palestinian Territory, Occupied'), ('PA', 'Panama'), ('PG', 'Papua New Guinea'), ('PY', 'Paraguay'), ('PE', 'Peru'), ('PH', 'Philippines'), ('PN', 'Pitcairn'), ('PL', 'Poland'), ('PT', 'Portugal'), ('PR', 'Puerto Rico'), ('QA', 'Qatar'), ('RE', 'Reunion'), ('RO', 'Romania'), ('RU', 'Russian Federation'), ('RW', 'Rwanda'), ('BL', 'Saint Barthelemy'), ('SH', 'Saint Helena, Ascension & Tristan Da Cunha'), ('KN', 'Saint Kitts and Nevis'), ('LC', 'Saint Lucia'), ('MF', 'Saint Martin (French Part)'), ('PM', 'Saint Pierre and Miquelon'), ('VC', 'Saint Vincent And The Grenadines'), ('WS', 'Samoa'), ('SM', 'San Marino'), ('ST', 'Sao Tome And Principe'), ('SA', 'Saudi Arabia'), ('SN', 'Senegal'), ('RS', 'Serbia'), ('SC', 'Seychelles'), ('SL', 'Sierra Leone'), ('SG', 'Singapore'), ('SX', 'Sint Maarten (Dutch Part)'), ('SK', 'Slovakia'), ('SI', 'Slovenia'), ('SB', 'Solomon Islands'), ('SO', 'Somalia'), ('ZA', 'South Africa'), ('GS', 'South Georgia And The South Sandwich Islands'), ('ES', 'Spain'), ('LK', 'Sri Lanka'), ('SD', 'Sudan'), ('SR', 'Suriname'), ('SJ', 'Svalbard And Jan Mayen'), ('SZ', 'Swaziland'), ('SE', 'Sweden'), ('CH', 'Switzerland'), ('SY', 'Syrian Arab Republic'), ('TW', 'Taiwan'), ('TJ', 'Tajikistan'), ('TZ', 'Tanzania'), ('TH', 'Thailand'), ('TL', 'Timor-Leste'), ('TG', 'Togo'), ('TK', 'Tokelau'), ('TO', 'Tonga'), ('TT', 'Trinidad and Tobago'), ('TN', 'Tunisia'), ('TR', 'Turkey'), ('TM', 'Turkmenistan'), ('TC', 'Turks And Caicos Islands'), ('TV', 'Tuvalu'), ('UG', 'Uganda'), ('UA', 'Ukraine'), ('AE', 'United Arab Emirates'), ('GB', 'United Kingdom'), ('US', 'United States'), ('UM', 'United States Minor Outlying Islands'), ('UY', 'Uruguay'), ('UZ', 'Uzbekistan'), ('VU', 'Vanuatu'), ('VE', 'Venezuela, Bolivarian Republic Of'), ('VN', 'Viet Nam'), ('VG', 'Virgin Islands, British'), ('VI', 'Virgin Islands, U.S.'), ('WF', 'Wallis and Futuna'), ('EH', 'Western Sahara'), ('YE', 'Yemen'), ('ZM', 'Zambia'), ('ZW', 'Zimbabwe')], verbose_name='Country')),
            ],
            options={
                'verbose_name': 'Billing Address',
                'verbose_name_plural': 'Billing Addresses',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('extra', shop.models.fields.JSONField(verbose_name='Arbitrary information for this cart')),
                ('billing_address', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='myshop.BillingAddress')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.CharField(blank=True, help_text='Product code of added item.', max_length=255, null=True, verbose_name='Product code')),
                ('extra', shop.models.fields.JSONField(verbose_name='Arbitrary information for this cart item')),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='myshop.Cart')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('recognized', shop.models.fields.ChoiceEnumField(help_text='Designates the state the customer is recognized as.', verbose_name='Recognized as')),
                ('last_access', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Last accessed')),
                ('extra', shop.models.fields.JSONField(editable=False, verbose_name='Extra information about this customer')),
                ('number', models.PositiveIntegerField(default=None, null=True, unique=True, verbose_name='Customer Number')),
                ('salutation', models.CharField(choices=[('mrs', 'Mrs.'), ('mr', 'Mr.'), ('na', '(n/a)')], max_length=5, verbose_name='Salutation')),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping_id', models.CharField(blank=True, help_text="The transaction processor's reference", max_length=255, null=True, verbose_name='Shipping ID')),
                ('fulfilled_at', models.DateTimeField(blank=True, null=True, verbose_name='Fulfilled at')),
                ('shipped_at', models.DateTimeField(blank=True, null=True, verbose_name='Shipped at')),
                ('shipping_method', models.CharField(help_text='The shipping backend used to deliver the items for this order', max_length=50, verbose_name='Shipping method')),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0, verbose_name='Delivered quantity')),
                ('delivery', models.ForeignKey(help_text='Refer to the shipping provider used to ship this item', on_delete=django.db.models.deletion.CASCADE, to='myshop.Delivery', verbose_name='Delivery')),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='OperatingSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', django_fsm.FSMField(default='new', max_length=50, protected=True, verbose_name='Status')),
                ('currency', models.CharField(editable=False, help_text='Currency in which this order was concluded', max_length=7)),
                ('_subtotal', models.DecimalField(decimal_places=2, max_digits=30, verbose_name='Subtotal')),
                ('_total', models.DecimalField(decimal_places=2, max_digits=30, verbose_name='Total')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('extra', shop.models.fields.JSONField(help_text='Arbitrary information for this order object on the moment of purchase.', verbose_name='Extra fields')),
                ('stored_request', shop.models.fields.JSONField(help_text='Parts of the Request objects on the moment of purchase.')),
                ('number', models.PositiveIntegerField(default=None, null=True, unique=True, verbose_name='Order Number')),
                ('shipping_address_text', models.TextField(blank=True, help_text='Shipping address at the moment of purchase.', null=True, verbose_name='Shipping Address')),
                ('billing_address_text', models.TextField(blank=True, help_text='Billing address at the moment of purchase.', null=True, verbose_name='Billing Address')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='myshop.Customer', verbose_name='Customer')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
            bases=(shop.payment.defaults.ManualPaymentWorkflowMixin, shop.payment.defaults.CancelOrderWorkflowMixin, shop_stripe.payment.OrderWorkflowMixin, shop.shipping.delivery.PartialDeliveryWorkflowMixin, models.Model),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, help_text='Product name at the moment of purchase.', max_length=255, null=True, verbose_name='Product name')),
                ('product_code', models.CharField(blank=True, help_text='Product code at the moment of purchase.', max_length=255, null=True, verbose_name='Product code')),
                ('_unit_price', models.DecimalField(decimal_places=2, help_text='Products unit price at the moment of purchase.', max_digits=30, null=True, verbose_name='Unit price')),
                ('_line_total', models.DecimalField(decimal_places=2, help_text='Line total on the invoice at the moment of purchase.', max_digits=30, null=True, verbose_name='Line Total')),
                ('extra', shop.models.fields.JSONField(help_text='Arbitrary information for this order item', verbose_name='Extra fields')),
                ('quantity', models.IntegerField(verbose_name='Ordered quantity')),
                ('canceled', models.BooleanField(default=False, verbose_name='Item canceled ')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='myshop.Order', verbose_name='Order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', shop.money.fields.MoneyField(help_text='How much was paid with this particular transfer.', verbose_name='Amount paid')),
                ('transaction_id', models.CharField(help_text="The transaction processor's reference", max_length=255, verbose_name='Transaction ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Received at')),
                ('payment_method', models.CharField(help_text='The payment backend used to process the purchase', max_length=50, verbose_name='Payment method')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myshop.Order', verbose_name='Order')),
            ],
            options={
                'verbose_name': 'Order payment',
                'verbose_name_plural': 'Order payments',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('active', models.BooleanField(default=True, help_text='Is this product publicly visible.', verbose_name='Active')),
                ('product_name', models.CharField(max_length=255, verbose_name='Product Name')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('caption', djangocms_text_ckeditor.fields.HTMLField(blank=True, help_text="Short description used in the catalog's list view of products.", null=True, verbose_name='Caption')),
                ('order', models.PositiveIntegerField(db_index=True, verbose_name='Sort by')),
            ],
            options={
                'ordering': ('order',),
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
            bases=(shop.models.product.CMSPageReferenceMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.SmallIntegerField(default=0)),
                ('image', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.CASCADE, to='filer.Image')),
            ],
            options={
                'ordering': ['order'],
                'abstract': False,
                'verbose_name': 'Product Image',
                'verbose_name_plural': 'Product Images',
            },
        ),
        migrations.CreateModel(
            name='ProductPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.Page')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.SmallIntegerField(db_index=True, default=0, help_text='Priority for using this address')),
                ('name', models.CharField(max_length=1024, verbose_name='Full name')),
                ('address1', models.CharField(max_length=1024, verbose_name='Address line 1')),
                ('address2', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Address line 2')),
                ('zip_code', models.CharField(max_length=12, verbose_name='ZIP / Postal code')),
                ('city', models.CharField(max_length=1024, verbose_name='City')),
                ('country', shop.models.address.CountryField(choices=[('AF', 'Afghanistan'), ('AX', 'Aland Islands'), ('AL', 'Albania'), ('DZ', 'Algeria'), ('AS', 'American Samoa'), ('AD', 'Andorra'), ('AO', 'Angola'), ('AI', 'Anguilla'), ('AQ', 'Antarctica'), ('AG', 'Antigua And Barbuda'), ('AR', 'Argentina'), ('AM', 'Armenia'), ('AW', 'Aruba'), ('AU', 'Australia'), ('AT', 'Austria'), ('AZ', 'Azerbaijan'), ('BS', 'Bahamas'), ('BH', 'Bahrain'), ('BD', 'Bangladesh'), ('BB', 'Barbados'), ('BY', 'Belarus'), ('BE', 'Belgium'), ('BZ', 'Belize'), ('BJ', 'Benin'), ('BM', 'Bermuda'), ('BT', 'Bhutan'), ('BO', 'Bolivia, Plurinational State Of'), ('BQ', 'Bonaire, Saint Eustatius And Saba'), ('BA', 'Bosnia And Herzegovina'), ('BW', 'Botswana'), ('BV', 'Bouvet Island'), ('BR', 'Brazil'), ('IO', 'British Indian Ocean Territory'), ('BN', 'Brunei Darussalam'), ('BG', 'Bulgaria'), ('BF', 'Burkina Faso'), ('BI', 'Burundi'), ('KH', 'Cambodia'), ('CM', 'Cameroon'), ('CA', 'Canada'), ('CV', 'Cape Verde'), ('KY', 'Cayman Islands'), ('CF', 'Central African Republic'), ('TD', 'Chad'), ('CL', 'Chile'), ('CN', 'China'), ('CX', 'Christmas Island'), ('CC', 'Cocos (Keeling) Islands'), ('CO', 'Colombia'), ('KM', 'Comoros'), ('CG', 'Congo'), ('CD', 'Congo, The Democratic Republic Of The'), ('CK', 'Cook Islands'), ('CR', 'Costa Rica'), ('HR', 'Croatia'), ('CU', 'Cuba'), ('CW', 'Curacao'), ('CY', 'Cyprus'), ('CZ', 'Czech Republic'), ('DK', 'Denmark'), ('DJ', 'Djibouti'), ('DM', 'Dominica'), ('DO', 'Dominican Republic'), ('EC', 'Ecuador'), ('EG', 'Egypt'), ('SV', 'El Salvador'), ('GQ', 'Equatorial Guinea'), ('ER', 'Eritrea'), ('EE', 'Estonia'), ('ET', 'Ethiopia'), ('FK', 'Falkland Islands (Malvinas)'), ('FO', 'Faroe Islands'), ('FJ', 'Fiji'), ('FI', 'Finland'), ('FR', 'France'), ('GF', 'French Guiana'), ('PF', 'French Polynesia'), ('TF', 'French Southern Territories'), ('GA', 'Gabon'), ('GM', 'Gambia'), ('DE', 'Germany'), ('GH', 'Ghana'), ('GI', 'Gibraltar'), ('GR', 'Greece'), ('GL', 'Greenland'), ('GD', 'Grenada'), ('GP', 'Guadeloupe'), ('GU', 'Guam'), ('GT', 'Guatemala'), ('GG', 'Guernsey'), ('GN', 'Guinea'), ('GW', 'Guinea-Bissau'), ('GY', 'Guyana'), ('HT', 'Haiti'), ('HM', 'Heard Island and McDonald Islands'), ('VA', 'Holy See (Vatican City State)'), ('HN', 'Honduras'), ('HK', 'Hong Kong'), ('HU', 'Hungary'), ('IS', 'Iceland'), ('IN', 'India'), ('ID', 'Indonesia'), ('IR', 'Iran, Islamic Republic Of'), ('IQ', 'Iraq'), ('IE', 'Ireland'), ('IL', 'Israel'), ('IT', 'Italy'), ('CI', 'Ivory Coast'), ('JM', 'Jamaica'), ('JP', 'Japan'), ('JE', 'Jersey'), ('JO', 'Jordan'), ('KZ', 'Kazakhstan'), ('KE', 'Kenya'), ('KI', 'Kiribati'), ('KP', "Korea, Democratic People's Republic Of"), ('KR', 'Korea, Republic Of'), ('KS', 'Kosovo'), ('KW', 'Kuwait'), ('KG', 'Kyrgyzstan'), ('LA', "Lao People's Democratic Republic"), ('LV', 'Latvia'), ('LB', 'Lebanon'), ('LS', 'Lesotho'), ('LR', 'Liberia'), ('LY', 'Libyan Arab Jamahiriya'), ('LI', 'Liechtenstein'), ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('MO', 'Macao'), ('MK', 'Macedonia'), ('MG', 'Madagascar'), ('MW', 'Malawi'), ('MY', 'Malaysia'), ('MV', 'Maldives'), ('ML', 'Mali'), ('ML', 'Malta'), ('MH', 'Marshall Islands'), ('MQ', 'Martinique'), ('MR', 'Mauritania'), ('MU', 'Mauritius'), ('YT', 'Mayotte'), ('MX', 'Mexico'), ('FM', 'Micronesia'), ('MD', 'Moldova'), ('MC', 'Monaco'), ('MN', 'Mongolia'), ('ME', 'Montenegro'), ('MS', 'Montserrat'), ('MA', 'Morocco'), ('MZ', 'Mozambique'), ('MM', 'Myanmar'), ('NA', 'Namibia'), ('NR', 'Nauru'), ('NP', 'Nepal'), ('NL', 'Netherlands'), ('AN', 'Netherlands Antilles'), ('NC', 'New Caledonia'), ('NZ', 'New Zealand'), ('NI', 'Nicaragua'), ('NE', 'Niger'), ('NG', 'Nigeria'), ('NU', 'Niue'), ('NF', 'Norfolk Island'), ('MP', 'Northern Mariana Islands'), ('NO', 'Norway'), ('OM', 'Oman'), ('PK', 'Pakistan'), ('PW', 'Palau'), ('PS', 'Palestinian Territory, Occupied'), ('PA', 'Panama'), ('PG', 'Papua New Guinea'), ('PY', 'Paraguay'), ('PE', 'Peru'), ('PH', 'Philippines'), ('PN', 'Pitcairn'), ('PL', 'Poland'), ('PT', 'Portugal'), ('PR', 'Puerto Rico'), ('QA', 'Qatar'), ('RE', 'Reunion'), ('RO', 'Romania'), ('RU', 'Russian Federation'), ('RW', 'Rwanda'), ('BL', 'Saint Barthelemy'), ('SH', 'Saint Helena, Ascension & Tristan Da Cunha'), ('KN', 'Saint Kitts and Nevis'), ('LC', 'Saint Lucia'), ('MF', 'Saint Martin (French Part)'), ('PM', 'Saint Pierre and Miquelon'), ('VC', 'Saint Vincent And The Grenadines'), ('WS', 'Samoa'), ('SM', 'San Marino'), ('ST', 'Sao Tome And Principe'), ('SA', 'Saudi Arabia'), ('SN', 'Senegal'), ('RS', 'Serbia'), ('SC', 'Seychelles'), ('SL', 'Sierra Leone'), ('SG', 'Singapore'), ('SX', 'Sint Maarten (Dutch Part)'), ('SK', 'Slovakia'), ('SI', 'Slovenia'), ('SB', 'Solomon Islands'), ('SO', 'Somalia'), ('ZA', 'South Africa'), ('GS', 'South Georgia And The South Sandwich Islands'), ('ES', 'Spain'), ('LK', 'Sri Lanka'), ('SD', 'Sudan'), ('SR', 'Suriname'), ('SJ', 'Svalbard And Jan Mayen'), ('SZ', 'Swaziland'), ('SE', 'Sweden'), ('CH', 'Switzerland'), ('SY', 'Syrian Arab Republic'), ('TW', 'Taiwan'), ('TJ', 'Tajikistan'), ('TZ', 'Tanzania'), ('TH', 'Thailand'), ('TL', 'Timor-Leste'), ('TG', 'Togo'), ('TK', 'Tokelau'), ('TO', 'Tonga'), ('TT', 'Trinidad and Tobago'), ('TN', 'Tunisia'), ('TR', 'Turkey'), ('TM', 'Turkmenistan'), ('TC', 'Turks And Caicos Islands'), ('TV', 'Tuvalu'), ('UG', 'Uganda'), ('UA', 'Ukraine'), ('AE', 'United Arab Emirates'), ('GB', 'United Kingdom'), ('US', 'United States'), ('UM', 'United States Minor Outlying Islands'), ('UY', 'Uruguay'), ('UZ', 'Uzbekistan'), ('VU', 'Vanuatu'), ('VE', 'Venezuela, Bolivarian Republic Of'), ('VN', 'Viet Nam'), ('VG', 'Virgin Islands, British'), ('VI', 'Virgin Islands, U.S.'), ('WF', 'Wallis and Futuna'), ('EH', 'Western Sahara'), ('YE', 'Yemen'), ('ZM', 'Zambia'), ('ZW', 'Zimbabwe')], verbose_name='Country')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myshop.Customer')),
            ],
            options={
                'verbose_name': 'Shipping Address',
                'verbose_name_plural': 'Shipping Addresses',
            },
        ),
        migrations.CreateModel(
            name='SmartPhoneVariant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.CharField(max_length=255, unique=True, verbose_name='Product code')),
                ('unit_price', shop.money.fields.MoneyField(decimal_places=3, help_text='Net price for this product', verbose_name='Unit price')),
                ('storage', models.PositiveIntegerField(help_text='Internal storage in MB', verbose_name='Internal Storage')),
            ],
        ),
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='myshop.Product')),
                ('unit_price', shop.money.fields.MoneyField(decimal_places=3, help_text='Net price for this product', verbose_name='Unit price')),
                ('product_code', models.CharField(max_length=255, unique=True, verbose_name='Product code')),
                ('placeholder', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, slotname='Commodity Details', to='cms.Placeholder')),
            ],
            options={
                'verbose_name': 'Commodity',
                'verbose_name_plural': 'Commodities',
            },
            bases=('myshop.product',),
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('base_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='SmartCard',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='myshop.Product')),
                ('unit_price', shop.money.fields.MoneyField(decimal_places=3, help_text='Net price for this product', verbose_name='Unit price')),
                ('card_type', models.CharField(choices=[('SD', 'SD'), ('micro SD', 'micro SD'), ('SDXC', 'SDXC'), ('micro SDXC', 'micro SDXC'), ('SDHC', 'SDHC'), ('micro SDHC', 'micro SDHC'), ('SDHC II', 'SDHC II'), ('micro SDHC II', 'micro SDHC II')], max_length=15, verbose_name='Card Type')),
                ('speed', models.CharField(choices=[(b'4', '4 MB/s'), (b'20', '20 MB/s'), (b'30', '30 MB/s'), (b'40', '40 MB/s'), (b'48', '48 MB/s'), (b'80', '80 MB/s'), (b'95', '95 MB/s'), (b'280', '280 MB/s')], max_length=8, verbose_name='Transfer Speed')),
                ('product_code', models.CharField(max_length=255, unique=True, verbose_name='Product code')),
                ('storage', models.PositiveIntegerField(help_text='Storage capacity in GB', verbose_name='Storage Capacity')),
                ('description', djangocms_text_ckeditor.fields.HTMLField(help_text="Full description used in the catalog's detail view of Smart Cards.", verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Smart Card',
                'verbose_name_plural': 'Smart Cards',
            },
            bases=('myshop.product',),
            managers=[
                ('default_manager', django.db.models.manager.Manager()),
                ('objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='SmartPhoneModel',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='myshop.Product')),
                ('battery_type', models.PositiveSmallIntegerField(choices=[(1, 'Lithium Polymer (Li-Poly)'), (2, 'Lithium Ion (Li-Ion)')], verbose_name='Battery type')),
                ('battery_capacity', models.PositiveIntegerField(help_text='Battery capacity in mAh', verbose_name='Capacity')),
                ('ram_storage', models.PositiveIntegerField(help_text='RAM storage in MB', verbose_name='RAM')),
                ('wifi_connectivity', models.PositiveIntegerField(choices=[(1, '802.11 b/g/n')], help_text='WiFi Connectivity', verbose_name='WiFi')),
                ('bluetooth', models.PositiveIntegerField(choices=[(1, 'Bluetooth 4.0'), (2, 'Bluetooth 3.0'), (3, 'Bluetooth 2.1')], help_text='Bluetooth Connectivity', verbose_name='Bluetooth')),
                ('gps', models.BooleanField(default=False, help_text='GPS integrated', verbose_name='GPS')),
                ('width', models.DecimalField(decimal_places=1, help_text='Width in mm', max_digits=4, verbose_name='Width')),
                ('height', models.DecimalField(decimal_places=1, help_text='Height in mm', max_digits=4, verbose_name='Height')),
                ('weight', models.DecimalField(decimal_places=1, help_text='Weight in gram', max_digits=5, verbose_name='Weight')),
                ('screen_size', models.DecimalField(decimal_places=2, help_text='Diagonal screen size in inch', max_digits=4, verbose_name='Screen size')),
                ('description', djangocms_text_ckeditor.fields.HTMLField(help_text="Full description used in the catalog's detail view of Smart Phones.", verbose_name='Description')),
                ('operating_system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myshop.OperatingSystem', verbose_name='Operating System')),
            ],
            options={
                'verbose_name': 'Smart Phone',
                'verbose_name_plural': 'Smart Phones',
            },
            bases=('myshop.product',),
            managers=[
                ('default_manager', django.db.models.manager.Manager()),
                ('objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='productpage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myshop.Product'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myshop.Product'),
        ),
        migrations.AddField(
            model_name='product',
            name='cms_pages',
            field=models.ManyToManyField(help_text='Choose list view this product shall appear on.', through='myshop.ProductPage', to='cms.Page'),
        ),
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ManyToManyField(through='myshop.ProductImage', to='filer.Image'),
        ),
        migrations.AddField(
            model_name='product',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myshop.Manufacturer', verbose_name='Manufacturer'),
        ),
        migrations.AddField(
            model_name='product',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_myshop.product_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myshop.Product', verbose_name='Product'),
        ),
        migrations.AddField(
            model_name='deliveryitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myshop.OrderItem', verbose_name='Ordered item'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myshop.Order'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myshop.Product'),
        ),
        migrations.AddField(
            model_name='cart',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='myshop.Customer', verbose_name='Customer'),
        ),
        migrations.AddField(
            model_name='cart',
            name='shipping_address',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='myshop.ShippingAddress'),
        ),
        migrations.AddField(
            model_name='billingaddress',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myshop.Customer'),
        ),
        migrations.AddField(
            model_name='smartphonevariant',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='myshop.SmartPhoneModel', verbose_name='Smartphone Model'),
        ),
    ]
