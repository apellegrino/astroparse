======
README
======

A simple Python module for parsing strings of astronomical coordinates.

Still a work in progress; feel free to suggest changes.

.. code-block:: python

    >>> import astroparse
    >>> astroparse.sdss("J131027.46+182617.4")
    (197.61441666666664, 18.438166666666667)
    >>> astroparse.ra("13:10:27.46")
    197.61441666666664
    >>> astroparse.dec("+18:26:17.40")
    18.438166666666667
