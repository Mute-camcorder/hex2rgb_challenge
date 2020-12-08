import rgb

SAMPLE_HAPPY_COLOURS = {
        "#000000": {"r": 0,   "g": 0,   "b": 0},
        "#172957": {"r": 23,  "g": 41,  "b": 87},
        "#800000": {"r": 128, "g": 0,   "b": 0},
        "#F42069": {"r": 244, "g": 32,  "b": 105},
        "#f8c6fd": {"r": 248, "g": 198, "b": 253},
        "#ffFFff": {"r": 255, "g": 255, "b": 255},
    }

def test_hex_to_rgb_function():
    for k, v in SAMPLE_HAPPY_COLOURS.items():
        assert v == rgb.hex_to_rgb(k)


def test_create_by_hex():
    for hex_code, rgb_dict in SAMPLE_HAPPY_COLOURS.items():
        c = rgb.Colour(hex_code=hex_code)
        assert c.r == rgb_dict["r"]
        assert c.g == rgb_dict["g"]
        assert c.b == rgb_dict["b"]
        
def test_create_by_dict():
    for hex_code, rgb_dict in SAMPLE_HAPPY_COLOURS.items():
        c = rgb.Colour(rgb_dict=rgb_dict)
        assert c.to_hex_code().lower() == hex_code.lower()

        assert c.r == rgb_dict["r"]
        assert c.g == rgb_dict["g"]
        assert c.b == rgb_dict["b"]
        
