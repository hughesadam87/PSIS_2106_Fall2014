# Imports
# -------
from __future__ import division
import logging

LOGGER = logging.getLogger(__name__) #add module name manually

__author__ = "Your name here"
__email__ = "Your email here"
__date__ = "Date here"

# -------------------------------------------------------------------------
# Objective:
# ----------

#   - This is where we describe assignment
#       - Do A
#       - Do B
#       - Do C

# See Also
# --------

#   - Links and reminders to other assignment
# -------------------------------------------------------------------------



class CustomError(Exception):
    """ Rename to your own error"""


def main():
    NotImplemented


if __name__ == '__main__':

    if '-v' in sys.argv:
        logging.basicConfig(filename='_log-%s' %__name__, level=logging.DEBUG)
    else:
        logging.basicConfig()

    main()