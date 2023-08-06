"""
Script to convert any decimal to a tape-measure friendly fraction.
For any decimal that is doesn't elegantly reduce, it rounds up to
the nearest 64th.
"""

import sys
import csv
import math
from collections import OrderedDict

# import csv lookup table of 64th fractions
with open('conversion_table.csv', 'r', encoding="utf-8") as f:
    r = csv.reader(f)
    conversion_table = OrderedDict(r)

# csv is imported with all keys and values as strings. Must convert keys into floats
conversion_table = {float(key):value for key, value in conversion_table.items()}

def to_fraction(decimal_value):
    """Do the actual converrsion"""

    fraction = ""

    if decimal_value >= 1:
        (decimal, integr) = math.modf(decimal_value)
        fraction += str(int(integr)) + " "
        decimal_value = float(decimal)

        print(integr, decimal, fraction)



    # iterate through conversion table. if the decimal value is
    # larger than the key for the current loop, continue to the
    # next iteration and check again. Eventually, we will hit a
    # key that is LARGER than the input decimal value. We then
    # return the value for that key.
    #
    # e.g. .484375 < .49 < .5, so .49 rounds to 1/2 and we return
    #      that fraction

    for key in conversion_table:
        if decimal_value > key:
            continue
        else:
            fraction += conversion_table[key]
            return fraction
        
if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        raise SyntaxError('Must pass one float value')
    
    print (to_fraction(float(sys.argv[1])))
