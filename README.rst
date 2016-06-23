================
autouseragents
================


What is autouseragents module for?
------------------------------------

This module is for generating random, valid web navigator's User-Agent HTTP headers.


Usage Example
-------------

.. code:: python

    >>> from autouseragents.autouseragents import AutoUserAgents
    >>> mua = AutoUserAgents()
    # random_agent() returns just the agent string now, pay attention!
    >>> mua.random_agent()
    Mozilla/5.0 (X11; Linux i686; rv:2.0b3pre) Gecko/20100731 Firefox/4.0b3pre
    >>> mua.random_agent()
    ELinks (0.11.3; Linux 2.6.22-gentoo-r9 i686; 80x40)
    >>> mua.reset()
    >>> mua.reset("crawlerlist")
    >>> mua.random_agent()
    Mozilla/4.0 compatible FurlBot/Furl Search 2.0 (FurlBot; http://www.furl.net; wn.furlbot@looksmart.net)
    # What's new since v0.5.4:
    # What will suprise you comes now:
    >>> mua.reset("browserlist")
    >>> mua.filter("os", "linux").filter("browser", "firefox").random_agent()
    Mozilla/5.0 (X11; U; Linux i686; de-DE; rv:1.9.2.8) Gecko/20100725 Gentoo Firefox/3.6.8
    >>> mua.filter("os", "windows").filter("browser", "chrome").random_agent())
    Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.27 Safari/532.0
    >>> mua.filter("os", "mac").filter("browser", "apple").random_agent())
    Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr-fr) AppleWebKit/125.5 (KHTML, like Gecko) Safari/125.9


Installation
------------

Use pip:

.. code:: shell

    $ pip install -U autouseragents


Documentation
-------------

Documentation is available at https://github.com/brunobell/autouseragents/blob/master/README.rst


Contribution
============

Use github to submit bug,fix or wish request: https://github.com/brunobell/autouseragents/issues

