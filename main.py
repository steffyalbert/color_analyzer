from color_analysis import ColorAnalyzer
from color_name_finder import ColorNameFinder


if __name__ == "__main__":

    # colors_test_case1 = ["#AABBCC", "#154331", "#A0B1C2", "#000000", "#FFFFFF"]
    colors = ["#AABBCC", "#154331", "#A0B1C2", "#000000"]
    
    analyzer = ColorAnalyzer(ColorNameFinder())
    brightest_color = analyzer.find_brightest_color(colors)    
    is_exact_match_available, color_name = analyzer.get_brightest_color_name(brightest_color)

    if is_exact_match_available:
        print(f"The brightest color is: #{brightest_color}, called {color_name}")
    else:
        print(f"The brightest color is: {brightest_color}, and the closest matching color is called {color_name}")
