$$$
===

Use this Python library to convert amounts of nearly any currency into dollars. 

$$$ uses the `Open Exchange Rates <https://openexchangerates.org/>`__ currency data API as a backend. It caches the rates for you, and pulls in the new values hourly so that your data will
never be older than < 2 hours. For that, you will
be able to use the free plan.

Here's how to use it:

::

    $ pip install dollars
    $ export OXR_APP_ID=...  # Your freely achieved app id
    $ ipython

    In [1]: from dollars import dollar

    In [2]: dollar('EUR', 5)
    Out[2]: 5.271147845154761

Stop worrying, and start converting!
