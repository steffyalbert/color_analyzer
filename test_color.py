import pytest
from color import Color

def test_valid_hex():
    """Test valid hex color initialization"""
    color = Color("#AABBCC")
    assert color.hex_color == "AABBCC"

def test_invalid_hex():
    """Test invalid hex color raises ValueError"""
    with pytest.raises(ValueError):
        Color("ZZZZZZ")

def test_rgb_conversion():
    """Test RGB conversion from hex"""
    color = Color("#112233")
    assert color.get_rgb() == (17, 34, 51)

def test_brightness():
    """Test brightness calculation"""
    color = Color("#FFFFFF")  # Brightest color
    assert color.brightness == 255.0  # White should be very bright

def test_distance():
    """Test distance calculation between colors"""
    color1 = Color("#000000")
    color2 = Color("#FFFFFF")
    assert color2.distance(color1) == 441.6729559300637  # Should be max apart

def test_string():
    """Test to string method for color"""
    color = Color("#FFFFFF")
    assert color.__str__() == "FFFFFF (r=255, g=255, b=255)"  # Should be max apart