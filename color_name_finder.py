import requests
import numpy as np
from color import Color
from typing import Tuple, Dict


class ColorNameFinder:
    """Class to find the closest named color to a given hex value."""
    
    API_URL = "https://www.csscolorsapi.com/api/colors"

    def __init__(self):
        self.hex_to_color = self.__get_css_colors()

    def __get_css_colors(self) -> Dict[str, Color]:
        """Fetches CSS color data and returns a dictionary of hex values to color names."""
        try:
            response = requests.get(ColorNameFinder.API_URL)
            response.raise_for_status()
            return {color['hex'].upper() : Color(color['hex'].upper(), color['name']) for color in response.json().get('colors', [])}
        except requests.exceptions.RequestException as e:
            print(f"Error fetching color data: {e}")
            return {}
    
    def find_closest_color_name(self, color_to_find: Color) -> str:
        """Find the closest named color to the given hex color."""
        
        if color_to_find.hex_color in self.hex_to_color:
            return True, self.hex_to_color[color_to_find.hex_color].color_name
        
        closest_color = "Unknown"
        closest_distance = float('inf')        
        for other_coler in self.hex_to_color.values():
            distance = color_to_find.distance(other_coler)
            if distance < closest_distance:
                closest_distance, closest_color = distance, other_coler.color_name
        
        return False, closest_color