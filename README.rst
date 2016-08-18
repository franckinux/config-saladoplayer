config-saladoplayer project
===========================

This project enables to configure a virtual tour running under SaladoPlayer
(https://github.com/mstandio/SaladoPlayer). Its main configuration file is
written in Python.

Why I wrote this
----------------

At first, I wrote a Django application called django-saladoplayer
(https://github.com/franckinux/django-saladoplayer) for making my tour
configurations. It was very practical (thanks to Django admin interface) but I
had to use a Python hosting. As I added more panoramas, I exceeded the 10Gb
limit. So, I switched to a hosting featuring 100Gb storage without Python.
Django being unavailable, I had to generate my tour configuration offline,
that's why I started this project. Finally, I prefer this way of configuring
pararama tours.

Tour configuration
------------------

The tour configuration is made via a python module. The config.py file is an
example, it can be put anywhere else in the filesystem. The other .py files must
be left unchanged.

Some common settings are written in the ini file config.ini. You can manage
several ini files, just provide the "-c" or "--config" argument to select the
one you want. The config.ini file provided is the default configuration file.

Generating the config.xml file : ::

    python3 make-config.py /path/to/config.py > config.xml

Using a per tour configuration file : ::

    python3 /path/to/make-config.py -c /path/to/config.ini /path/to/config.py > config.xml

Examples
--------
