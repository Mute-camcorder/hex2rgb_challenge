# RGB.py
# This file should contain:
#   * a function that converts a hex code into a dictionary of r, g, b integers
#   * a class `Colour` that can be instantiated by hex code or by a dictionary of r, g, b integers;
#     - a method `to_hex_code()` that returns the hex representation
#     - a method `to_rgb_dict()` that returns the r, g, b values as integers in a dictionary
#
# Checkout test_color_class.py to see what is expected. Tests are run with `pytest`. You can (and should!) run the tests
# as often as you want.
#
# Feel free to look up *any* reference or information you need, ask any questions you want and importantly, have fun!


def hex_to_rgb(hex_code):
    """hi here is the code"""
    r_str = hex_code[1:3]
    g_str = hex_code[3:5]
    b_str = hex_code[5:]
    return {
        "r": int(r_str, base=16), 
        "g": int(g_str, base=16),
        "b": int(b_str, base=16)
    }

class Colour:
    pass

