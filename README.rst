SimpleConfigParser
==================

.. image:: https://travis-ci.org/helgi/python-simpleconfigparser.png
   :target: https://travis-ci.org/helgi/python-simpleconfigparser

Builds on top of the builtin SafeConfigParser but adds various
convenience functionalities.

-  Access to all the usual ConfigParser functionality
-  Access sections and items via convience objects and dicts instead of
   ``get()``
-  Makes accessing items and section via dicts possible on Python 2.7+,
   ConfigParser has that from Python 3.2 onwards as a default
-  Ability to set values via the objects
   ``config.section.item = 'demmmmm'`` and dicts
   ``config['section']['item']`` all while ``write()`` still work as
   normal
-  Make a few functions work directly from the section object
   ``config.section.items()``, ``config.section.getboolean('item')``
-  Strips any quotes on the edgeds of items used in the INI file instead
   of returning it as part of the values
-  Improve the defaults handling on the object to be more sensible

.. code:: python

    defaults = {
        'section': {
            'item1': 'boo',
            'item2': 'bar'
        }
    }

    config = simpleconfigparser(defaults=defaults)

Examples
========

contents of read.ini:
::

    [app]
    debug = yes

test.py:

.. code:: python

    from simpleconfigparser import simpleconfigparser

    config = simpleconfigparser()
    config.read('read.ini')

    print(config.app.debug)
    print(config.app.getboolean('debug'))
    print(config['app']['debug'])
    print(config['app'].getboolean('debug'))
    config.app.debug = no
    with open('new.ini', 'wb') as handle:
        config.write(handle)

License
=======
MIT - See LICENSE file