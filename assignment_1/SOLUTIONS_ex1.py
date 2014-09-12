# Imports
# -------
from __future__ import division
from math import pi as PI

__author__ = "Your name here"
__email__ = "Your email here"
__date__ = "Date here"

#--------------------------------------------------------------------------
# Objective:
# ----------

#   PART A:
#   - Create a function that computes the area of a circle given a radius.
#       - The function should return the area of the circle.
#       - Use the math library to import the exact value of pi.
#       - Make sure that if an int is passed to your function, the correct
#         area is still returned.
#   - In your main code, compute the area for a circle of radius 5, 10 and 15
#     and print a nice output such as "For radius = x, the circular area is y".

#   PART B:
#    - Create a function that measures the prints the length of a string, and 
#        prints the string converted to lowercase.  Print out 3 strings of your
#        choosing.
#    - Example input of "Hi I am a String" should result in something like:
#            "Converted length 17 string to lowercase: hi i am a string"

# See Also
# --------

# -------------------------------------------------------------------------



# Functions
# ---------
def areacircle(radius):
    """ Return area of a circle given the radius"""
    return PI * float(radius) ** 2


def lenstring(userstring):
    """ Prints length of string and converts to lowercase"""
    length = len(userstring)
    lower = userstring.lower()
    print "\nConverted length %s string to lowercase: %s" % (length, lower) 


if __name__ == '__main__':

    # Part A: Area
    # ---------
    for radius in [5, 10, 15]:
        area = areacircle(radius)
        print '\nFor radius = %s, the circular area is %s' % (radius, area)
        
    # Part B: String
    # ---------
    lenstring("What's up my Friends?")
    lenstring("HeLLo ClAriCE")
    lenstring("was lowercase anyway")
