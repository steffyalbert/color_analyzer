import math
import re

class Color:
    def __init__(self, hex_color, color_name=None):
        self.hex_color = hex_color.lstrip("#")
        if(not self.__is_valid_hex_color()):
            raise ValueError(f"Invalid hex color: {self.hex_color}")
        self.color_name = color_name
        self.red, self.green, self.blue = self.__split_rgb_components()
        self.brightness = self.__calculate_brightness()

    def __is_valid_hex_color(self):
        """Check if a color is a valid hex color code """
        
        # Check if the color matches valid hex color patterns
        # Supports 3 or 6 character hex codes
        hex_pattern = r'^([0-9A-Fa-f]{3}|[0-9A-Fa-f]{6})$'
        
        return bool(re.match(hex_pattern, self.hex_color))

    def __hex_to_decimal(self, hex_color):
        """Convert hex color to an decimal value."""
        return int(hex_color.lstrip('#'), 16)
    
    def __split_rgb_components(self):
        """Extract RGB components from the hex color."""
        red = self.__hex_to_decimal(self.hex_color[0:2])
        green = self.__hex_to_decimal(self.hex_color[2:4])
        blue = self.__hex_to_decimal(self.hex_color[4:])
        return red, green, blue
    
    def __calculate_brightness(self):
        """Calculate the brightness of a color using the given formula."""
        return math.sqrt(0.241 * self.red**2 + 0.691 * self.green**2 + 0.068 * self.blue**2)
    
    def get_rgb(self):
        """Return the RGB components."""
        return self.red, self.green, self.blue
    
    def distance(self, color) -> float:
        """Calculate Euclidean distance between two colors in RGB space."""
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(self.get_rgb(), color.get_rgb())))

    def __str__(self):
        """String representation of the color in hex format."""
        return f"{self.hex_color} (r={self.red}, g={self.green}, b={self.blue})"
