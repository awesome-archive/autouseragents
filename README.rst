================
auto_user_agents
================


What is auto_user_agents module for?
------------------------------------

This module is for generating random, valid web navigator's User-Agent HTTP headers.


Usage Example
-------------

.. code:: python

    >>> from autouseragents.auto_user_agents import AutoUserAgents
    >>> mua = AutoUserAgents()
    >>> mua.random_agent()
    {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:2.0b3pre) Gecko/20100731 Firefox/4.0b3pre'}
    >>> mua.random_agent()
    {'User-Agent': 'ELinks (0.11.3; Linux 2.6.22-gentoo-r9 i686; 80x40)'}
    >>> mua.reset()
    >>> mua.reset("crawlerlist")
    >>> mua.random_agent()
    {'User-Agent': u'Mozilla/4.0 compatible FurlBot/Furl Search 2.0 (FurlBot; http://www.furl.net; wn.furlbot@looksmart.net)'}


Installation
------------

Use pip:

.. code:: shell

    $ pip install autouseragents


Documentation
-------------

Documentation is available at https://github.com/brunobell/python-auto-user-agents/blob/master/README.rst


Contribution
============

Use github to submit bug,fix or wish request: https://github.com/brunobell/python-auto-user-agents/issues

