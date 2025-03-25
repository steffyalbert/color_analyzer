import pytest
from color_analysis import ColorAnalyzer
from color_name_finder import ColorNameFinder
from color import Color

class MockColorNameFinder:
    """Mock version of ColorNameFinder for testing without API calls."""
    def find_closest_color_name(self, color):
        return False, "Mocked Color"

@pytest.fixture
def analyzer():
    """Fixture to create a ColorAnalyzer instance with a mock ColorNameFinder"""
    return ColorAnalyzer(MockColorNameFinder())

def test_find_brightest_color(analyzer):
    """Test finding the brightest color"""
    colors = ["#AABBCC", "#154331", "#FFFFFF"]
    brightest = analyzer.find_brightest_color(colors)
    
    assert str(brightest) == "FFFFFF (r=255, g=255, b=255)"  # Should be white

def test_get_closest_brightest_color_name(analyzer):
    """Test fetching the name of the brightest color"""
    color = Color("#FFFFFF")
    is_exact, name = analyzer.get_brightest_color_name(color)
    
    assert not is_exact  # Mocked behavior
    assert name == "Mocked Color"