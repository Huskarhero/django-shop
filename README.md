# django-SHOP

[![Build Status](https://travis-ci.org/awesto/django-shop.svg?branch=master)](https://travis-ci.org/awesto/django-shop?branch=master)
[![PyPI version](https://img.shields.io/pypi/v/django-shop.svg)](https://pypi.python.org/pypi/django-shop)
[![Join the chat at https://gitter.im/awesto/django-shop](https://badges.gitter.im/awesto/django-shop.svg)](https://gitter.im/awesto/django-shop?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Software license](https://img.shields.io/pypi/l/django-shop.svg)](https://pypi.python.org/pypi/django-shop)
[![Twitter Follow](https://img.shields.io/twitter/follow/djangoSHOP.svg?style=social&label=djangoSHOP)](https://twitter.com/djangoSHOP)

**Django-SHOP** aims to be a the easy, fun and fast e-commerce counterpart to
[django-CMS](https://www.django-cms.org/).

Here you can find the [full documentation for django-SHOP](https://django-shop.readthedocs.io/en/latest/).

## Version 1.1 has been released!

See below on how to install it using the Cookiecutter template.


## Build the database model out of the product's properties – not vice versa

Most e-commerce systems are shipped with a predefined database model for products. But products can
vary a lot, and it simply is impossible to create a model which fits for all of them. This is
esspecially true for products with a hierarchy of variants. In many popular e-commerce platforms,
you either have far too many attributes per product, and/or the really required attributes are
missing.

In **django-SHOP** implementations, the product models reflect their pysical properties making it
possible to create complete and deep hierarchies of variations, but without having to fiddle with
unneeded properties. It furthermore avoids the need for an
[Entity Attribute Value Model](https://en.wikipedia.org/wiki/Entity–attribute–value_model), which
is considered a database anti-pattern, because it produces far too many table joins, when filtering
by property.


## Don't build pages using hard-coded templates – compose them

With the advent of frameworks, such as Angular, React, Vue and Aurelia, building web-applications
shifted from a page-centric to a component-based approach.

In **django-SHOP**, you are in full control over the page's layout, since all components are
encapsulated and independent from each other. This means that instead of adopting the Catalog, Cart,
Checkout and Order pages, use the **django-CMS** plugin system to compose everything required for
those pages.


## All Views are either HTML or RESTful services

Browser based navigation is important, but nowadays it's only one of many channels, clients
communicate with a web-server. Consider Single Page Applications or other native clients, where we
use RESTful APIs instead of pure HTTP.

This strongly reduces the payload having to be transferred. It furthermore gives the client a
smoother user experience, since only the content has to be updated, rather than having to do full
page reloads.


## Programmable cart modifiers

During checkout, taxes have to be applied or attributed. Depending on the shipping destination, the
product group and other factors, this computation can either be simple or quite demanding.
**Django-SHOP** offers a pluggable interface, to create modifiers which calculate the cart's totals,
taxes and other costs.

This same interface can be extended to compute the weight and shipping costs. It also can be used
for subtracting discounts or to add additional charges. 


## Programmable workflow for fulfilment and delivery

Fulfilling and shipping orders, probably is that part in e-commerce, which requires the most
individual adaption. **Django-SHOP** offers a programmable interface for orders, by using a finite
state machine to adopt the workflow. Each order may have several states, but only those actions
may be performed, for which state transitions are explicitly possible.


## It's modular

Whenever possible, extra features shall be added to third party libraries. This implies that
**django-SHOP** aims to provide an API, which allows merchants to add every feature they desire.

Currently there are third party libraries for several Payment Service Providers, such as
[PayPal](https://developer.paypal.com/docs/api/overview/), [Stripe](https://stripe.com/docs/api),
[BS-PayOne](https://www.bspayone.com/DE/en) and [Viveum](https://www.viveum.com/?lang=en).
An open interface allows you to add any other provider.

Shipping Service Providers may be added as third party library as well. With
[SendCloud](https://docs.sendcloud.sc/), ship your orders using one or more parcel services
available for your region.


## Start by building your own demo

Instead of providing an accessible online demo, **django-SHOP** can be set up in less than three
minutes, and preconfigured to your needs. Having access to the product models, you can immediate
start to play arround, rename them, and modify them to reflect the properties of your products.
This is the easiest way to get a shop up and running out of the box, with the flexibility of a
web-site which could have been built from scratch by yourself.

If you want to start with a fresh demo, please use the prepared
[Cookiecutter template for django-SHOP](https://github.com/awesto/cookiecutter-django-shop)
and follow the instructions. 

To get a first impression of the upcoming release 1.1, please use this
[Cookiecutter template for django-SHOP version 1.1](https://github.com/awesto/cookiecutter-django-shop/tree/releases/1.1)


## Audience of django-SHOP users

Specifically, we aim at providing a clean, modular and Pythonic/Djangonic implementation of an
e-commerce framework, that a moderately experienced Django developer should be able to pick up
and run easily. Pure Django models are used to describe each product type, and so the Django admin
shall be used to build a minimalistic editor for each of them.


## Consultancy

We provide full consultancy support and are available for building complete e-commerce systems based
on **django-SHOP**. Please contact office@awesto.com for further questions.


## Documentation

Read the full documentation on Read-the-docs:

[https://django-shop.readthedocs.io/en/latest/](https://django-shop.readthedocs.io/en/latest/)
