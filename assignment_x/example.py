__author__ = "Adam Hughes"
__email__ = "hugadams@gwmail.gwu.edu"
__date__ = "9/8/14"

#--------------------------------------------------------------------------
# Objective:
# ----------

#   - Create a function that lowercases a string
#       - Must have a clear docstring
#       - Must print out how many letters were changed

# See Also
# --------

#   - String.lower()
#       http://www.tutorialspoint.com/python/string_lower.htm
# -------------------------------------------------------------------------


# Imports
# -------
from __future__ import division


# Classes
# ---------
class BadStringError(Exception):
    """ User passes a non-string"""


# Functions
# ---------

def countlower(s):
    """ Given a string, s, returns the lower-case version and prints the
    number of letters that were case-converted.
    """
    
    try:
        lower = s.lower()
    except AttributeError:
        raise BadStringError('%s is not a string')
    
    # Count number of non-lower case strings
    count = len([i for i in lower if i not in s])
    print 'Found %s case-converted strings in %s' % (count, s)

if __name__ == '__main__':

    # Main Code
    # ---------
    countlower(s)