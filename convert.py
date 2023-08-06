from collections import OrderedDict

conversion_table = OrderedDict({
    .0      : "0",
    .015625 : "1/64",
    .03125  : "1/32",
    .046875 : "3/64",
    .0625   : "1/16",
    .078125 : "5/64",
    .09375  : "3/32",
    .109375 : "7/64",
    .125    : "1/8"
})

def to_fraction(dec):
    fraction = ""
    for key in conversion_table:
        fraction = conversion_table[key]
        if dec > key:
            continue
        else:
            return fraction

print (to_fraction(.1092))
