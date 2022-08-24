
# Start by importing our `rgb.py` file which we plan on testing
import rgb

SAMPLE_HAPPY_COLOURS = {
        "#000000": {"r": 0,   "g": 0,   "b": 0},
        "#0FA5FF": {"r": 15,  "g": 165, "b": 255},
        "#172957": {"r": 23,  "g": 41,  "b": 87},
        "#800000": {"r": 128, "g": 0,   "b": 0},
        "#F42069": {"r": 244, "g": 32,  "b": 105},
        "#f8c6fd": {"r": 248, "g": 198, "b": 253},
        "#ffFFff": {"r": 255, "g": 255, "b": 255},
    }

class TestPureFunctions:
    def test_hex_to_rgb(self):
        for k, v in SAMPLE_HAPPY_COLOURS.items():
            assert v == rgb.hex_to_rgb(k)

class TestColourClassSixHappy:
    """
    This class tests the `Colour` class, and only tests the 'happy-path'
    """

    def test_instantiate_by_hex(self):
        """
        Can we instantiate a Colour class with a 6 digit hex code as input? No Validation
        """
        for hex_code, rgb_dict in SAMPLE_HAPPY_COLOURS.items():
            c = rgb.Colour(hex_code=hex_code)
            assert type(c) == rgb.Colour

    def test_instantiate_by_dict(self):
        """
        Can we instantiate a Colour class with a dictionary as input? No Validation
        """
        for hex_code, rgb_dict in SAMPLE_HAPPY_COLOURS.items():
            c = rgb.Colour(rgb_dict=rgb_dict)
            assert type(c) == rgb.Colour

    def test_hex_code_object_to_hex_code(self):
        """
        Creates Colours using hex codes, then validates that the `to_hex_code` method returns the right value
        """
        for hex_code, rgb_dict in SAMPLE_HAPPY_COLOURS.items():
            c = rgb.Colour(hex_code=hex_code)
            # Note the test here calls `lower` because we don't have a perference for if the output is upper or lower
            assert c.to_hex_code().lower() == hex_code.lower()

    def test_rgb_dict_object_to_hex_code(self):
        """
        Creates Colours using rgb_dicts, then validates that the `to_hex_code` method returns the right value
        """
        for hex_code, rgb_dict in SAMPLE_HAPPY_COLOURS.items():
            c = rgb.Colour(rgb_dict=rgb_dict)
            # Note the test here calls `lower` because we don't have a perference for if the output is upper or lower
            assert c.to_hex_code().lower() == hex_code.lower()

    def test_hex_code_object_to_rgb_dict(self):
        """
        Creates colours using a dictionary, and calls `rgb_dict`, validating the output
        """
        for hex_code, rgb_dict in SAMPLE_HAPPY_COLOURS.items():
            c = rgb.Colour(hex_code=hex_code)
            assert c.to_rgb_dict() == rgb_dict

    def test_rgb_dict_object_to_rgb_dict(self):
        """
        Creates colours using a dictionary, and calls `rgb_dict`, validating the output
        """
        for hex_code, rgb_dict in SAMPLE_HAPPY_COLOURS.items():
            c = rgb.Colour(rgb_dict=rgb_dict)
            assert c.to_rgb_dict() == rgb_dict


class TestColourClassComparisons:
    """
    This class tests the `Colour` class, and only tests that two colours with the same values compare equally.
    """

    def test_same_hex_code_colours_compare_equal(self):
        """
        Can we instantiate two Colours with the same hex code, and have them compare equal?
        """
        for hex_code, rgb_dict in SAMPLE_HAPPY_COLOURS.items():
            c1 = rgb.Colour(hex_code=hex_code)
            c2 = rgb.Colour(hex_code=hex_code)
            assert c1 == c2

    def test_same_rgb_dict_colours_compare_equal(self):
        """
        Can we instantiate two Colours with the same rgb dict, and have them compare equal?
        """
        for hex_code, rgb_dict in SAMPLE_HAPPY_COLOURS.items():
            c1 = rgb.Colour(rgb_dict=rgb_dict)
            c2 = rgb.Colour(rgb_dict=rgb_dict)
            assert c1 == c2

    def test_matching_colours_hex_on_left_rgb_on_right_compare_equal(self):
        """
        Can we instantiate two equal Colours with both input types, and have them compare equal?
        """
        for hex_code, rgb_dict in SAMPLE_HAPPY_COLOURS.items():
            c1 = rgb.Colour(hex_code=hex_code)
            c2 = rgb.Colour(hex_code=hex_code)
            assert c1 == c2

    def test_matching_colours_hex_on_right_rgb_on_left_compare_equal(self):
        """
        Can we instantiate two equal Colours with both input types, and have them compare equal?
        """
        for hex_code, rgb_dict in SAMPLE_HAPPY_COLOURS.items():
            c1 = rgb.Colour(hex_code=hex_code)
            c2 = rgb.Colour(rgb_dict=rgb_dict)
            assert c1 == c2

    def test_different_colours_compare_not_equal(self):
        c1 = rgb.Colour(hex_code="#010203")
        c2 = rgb.Colour(hex_code="#01020F")
        assert c1 != c2