from color_name_finder import ColorNameFinder
from color import Color
    
class ColorAnalyzer:
    """Class to find the brightest color the corresponding color name"""
    def __init__(self, color_name_finder):
        self.color_name_finder = color_name_finder
    
    def find_brightest_color(self, hexa_color_codes):
        """Find the brightest color in the list"""
        colors = [Color(color) for color in hexa_color_codes]
        return max(colors, key=lambda color: color.brightness)    
    
    def get_brightest_color_name(self, color):
        """Returns the color name of the brightest color from the list."""
        is_exact_match_available, color_name = self.color_name_finder.find_closest_color_name(color)
        # Return the availability and the color name
        return is_exact_match_available, color_name
    

