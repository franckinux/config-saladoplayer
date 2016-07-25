This project enables to configure a virtual tour using SaladoPlayer
(https://github.com/mstandio/SaladoPlayer).

At first, I wrote a Django application called django-saladoplayer
(https://github.com/franckinux/django-saladoplayer) for making my tour
configurations. It was very practical (thanks to Django admin interface) but I
had to use a Python hosting that offered a 10Gb storage. As I added more
panoramas, I exceeded the 10Gb limit. So, I switched to a static hosting with
100Gb storage. I had to generate my tour configuration offline, that's my I
started this project. Finilly, I prefer this way of configuring pararama tours.

The tour configuration is made via a python file called config.py.

Running the example :

python3 make-config.py
