This project enables to configure a virtual tour using SaladoPlayer
(https://github.com/mstandio/SaladoPlayer).

At first, I wrote a Django application called django-saladoplayer
(https://github.com/franckinux/django-saladoplayer) for making my tour
configurations. It was very practical (thanks to Django admin interface) but I
had to use a Python hosting that offered a 10Gb storage. As I added more
panoramas, I exceeded the 10Gb limit. So, I switched to a static hosting with
100Gb storage. I had to generate my tour configuration offline, that's my I
started this project. Finally, I prefer this way of configuring pararama tours.

The tour configuration is made via a python module. The config.py file is an
example, it can be put anywhere else in the filesystem. The other .py files must
be left unchanged.

Some common settings are written in the ini file config.ini. You can can manage
several ini files, just provide the "-c" or "--config" argument to select the
one you want. The config.ini file provided is the default configuration file.

Running the example : ::

    python3 make-config.py /path/to/config.py > config.xml

Running a more general case : ::

    python3 /path/to/make-config.py -c /path/to/config.ini /path/to/config.py > config.xml
