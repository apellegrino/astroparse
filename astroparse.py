import re

patterns = {
    'sdss': re.compile(
                    r'J(?P<rhr>\d\d)'
                    r'(?P<rmin>\d\d)'
                    r'(?P<rsec>\d\d\.\d\d)'
                    r'(?P<dsign>[\+-])'
                    r'(?P<ddeg>\d\d)'
                    r'(?P<dmin>\d\d)'
                    r'(?P<dsec>\d\d\.\d)'
                        ),

    'colon': re.compile(
                    r'^(?P<sign>[\+-]?)'
                    # unit is either degrees (DEC) or hours (RA)
                    r'(?P<unit>\d?\d):'
                    r'(?P<min>\d\d):'
                    # do not capture digits past decimal as own group
                    r'(?P<sec>\d\d(?:\.\d*)?)'
                        ),
        }

def sdss(string):
    """Convert a string containing an SDSS object name to (ra, dec) decimal
    degrees.
    """
    match = patterns['sdss'].search(string)

    if not match:
        raise ValueError(
        "No SDSS name match found for string \"{}\"".format(string)
                        )

    rhr = float(match.group('rhr'))
    rmin = float(match.group('rmin'))
    rsec = float(match.group('rsec'))
    dsign = match.group('dsign')
    ddeg = float(match.group('ddeg'))
    dmin = float(match.group('dmin'))
    dsec = float(match.group('dsec'))

    if dsign == '':
        raise ValueError("No sign found in SDSS name \"{}\"".format(s))

    ra = (rhr + rmin/60. + rsec/60./60.) * 15.
    dec = (ddeg + dmin/60. + dsec/60./60.)

    if dsign == '-':
        dec *= -1.

    return ra, dec

def ra(string):
    """Convert a string containing sexagesimal RA to decimal degrees."""
    match = patterns['colon'].search(string)

    if not match:
        raise ValueError(
        "No RA match found for string \"{}\"".format(string)
                        )

    hrs = float(match.group('unit'))
    min = float(match.group('min'))
    sec = float(match.group('sec'))
    
    decimal = ( hrs + min/60. + sec/60./60. )

    decimal *= 15.

    return decimal

def dec(string):
    """Convert a string containing sexagesimal DEC to decimal degrees."""
    match = patterns['colon'].search(string)

    if not match:
        raise ValueError(
        "No DEC match found for string \"{}\"".format(string)
                        )

    sign = match.group('sign')
    deg = float(match.group('unit'))
    min = float(match.group('min'))
    sec = float(match.group('sec'))
    
    decimal = ( deg + min/60. + sec/60./60. )

    if sign == '-':
        decimal *= -1.

    return decimal
