import pytest
from unittest.mock import patch
from color_name_finder import ColorNameFinder
from color import Color

@pytest.fixture
def mock_api_response():
    return {
        "colors": [
            {"hex": "#FFFFFF", "name": "White"},
            {"hex": "#000000", "name": "Black"}
        ]
    }

@patch("color_name_finder.requests.get")
def test_get_css_colors(mock_get, mock_api_response):
    """Test API call and parsing of color data"""
    mock_get.return_value.json.return_value = mock_api_response
    mock_get.return_value.status_code = 200

    finder = ColorNameFinder()
    assert "#FFFFFF" in finder.hex_to_color
    assert finder.hex_to_color["#FFFFFF"].color_name == "White"

def test_find_closest_color():
    """Test closest color finding logic"""
    finder = ColorNameFinder()
    finder.hex_to_color = {
        "#FFFFFF": Color("#FFFFFF", "White"),
        "#000000": Color("#000000", "Black"),
    }
    color_to_find = Color("#F0F0F0")
    is_exact, closest_name = finder.find_closest_color_name(color_to_find)
    
    assert not is_exact  # Not an exact match
    assert closest_name == "White"  # Closest should be White