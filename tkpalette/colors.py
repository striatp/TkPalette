from typing import Tuple, Union

class COLOR:
    """
    A class to represent and manage colors in hex and RGB formats.
    """
    black = '#000000'
    white = '#FFFFFF'
    red = '#FF0000'
    green = '#00FF00'
    blue = '#0000FF'
    yellow = '#FFFF00'
    orange = '#FFA500'
    purple = '#800080'
    pink = '#FFC0CB'
    brown = '#A52A2A'
    gray = '#808080'
    cyan = '#00FFFF'
    magenta = '#FF00FF'
    lime = '#00FF00'
    teal = '#008080'
    indigo = '#4B0082'
    violet = '#EE82EE'
    turquoise = '#40E0D0'
    peach = '#FFDAB9'
    mint = '#98FF98'
    salmon = '#FA8072'
    ivory = '#FFFFF0'
    gold = '#FFD700'
    silver = '#C0C0C0'
    bronze = '#CD7F32'
    ruby = '#E0115F'
    emerald = '#50C878'
    sapphire = '#0F52BA'
    plum = '#DDA0DD'
    lavender = '#E6E6FA'
    chocolate = '#D2691E'
    tan = '#D2B48C'
    beige = '#F5F5DC'
    coral = '#FF7F50'
    crimson = '#DC143C'
    navy = '#000080'
    olive = '#808000'
    maroon = '#800000'
    azure = '#F0FFFF'
    rose = '#FF007F'
    amber = '#FFBF00'
    apricot = '#FBCEB1'
    aquamarine = '#7FFFD4'
    bistre = '#3D2B1F'
    blush = '#DE5D83'
    carmine = '#960018'
    chartreuse = '#7FFF00'
    cobalt = '#0047AB'
    copper = '#B87333'
    denim = '#1560BD'
    ebony = '#555D50'
    firebrick = '#B22222'
    forestgreen = '#228B22'
    fuchsia = '#FF00FF'
    khaki = '#F0E68C'
    lemonchiffon = '#FFFACD'
    linen = '#FAF0E6'
    moccasin = '#FFE4B5'
    orchid = '#DA70D6'
    papayawhip = '#FFEFD5'
    peru = '#CD853F'
    rebeccapurple = '#663399'
    seashell = '#FFF5EE'
    sienna = '#A0522D'
    slateblue = '#6A5ACD'
    slategray = '#708090'
    snow = '#FFFAFA'
    springgreen = '#00FF7F'
    steelblue = '#4682B4'
    thistle = '#D8BFD8'
    tomato = '#FF6347'
    wheat = '#F5DEB3'
    yellowgreen = '#9ACD32'
    aliceblue = '#F0F8FF'
    antiquewhite = '#FAEBD7'
    aquamarine = '#7FFFD4'
    burlywood = '#DEB887'
    cadetblue = '#5F9EA0'
    chartreuse = '#7FFF00'
    darkgoldenrod = '#B8860B'
    darkgray = '#A9A9A9'
    darkkhaki = '#BDB76B'
    darkmagenta = '#8B008B'
    darkolivegreen = '#556B2F'
    darkorange = '#FF8C00'
    darkorchid = '#9932CC'
    darkred = '#8B0000'
    darksalmon = '#E9967A'
    darkseagreen = '#8FBC8F'
    darkslateblue = '#483D8B'
    darkslategray = '#2F4F4F'
    darkturquoise = '#00CED1'
    dodgerblue = '#1E90FF'
    firebrick = '#B22222'
    floralwhite = '#FFFAF0'
    gainsboro = '#DCDCDC'
    ghostwhite = '#F8F8FF'
    honeydew = '#F0FFF0'
    hotpink = '#FF69B4'
    indianred = '#CD5C5C'
    lawngreen = '#7CFC00'
    lightcoral = '#F08080'
    lightgoldenrodyellow = '#FAFAD2'
    lightgreen = '#90EE90'
    lightpink = '#FFB6C1'
    lightsteelblue = '#B0C4DE'
    mediumaquamarine = '#66CDAA'
    mediumseagreen = '#3CB371'
    mediumslateblue = '#7B68EE'
    mediumspringgreen = '#00FA9A'
    midnightblue = '#191970'
    mistyrose = '#FFE4E1'
    oldlace = '#FDF5E6'

    # Initialisation
    def __init__(self, color: Union[str, Tuple[int, int, int]]) -> None:
        """
        Initialize a COLOR instance with a color in hex or RGB format.

        Args:
            color (Union[str, Tuple[int, int, int]]): A hex color string (e.g., "#FF5733") 
                                                     or an RGB tuple (e.g., (255, 87, 51)).

        Raises:
            ValueError: If the color format is invalid.
        """
        self.color = self._validate_color(color)

    # Method to validate the color format
    def _validate_color(self, color: Union[str, Tuple[int, int, int]]) -> str:
        """
        Validate the color format and convert to hex if needed.

        Args:
            color (Union[str, Tuple[int, int, int]]): The color to validate.

        Returns:
            str: A valid hex color string.

        Raises:
            ValueError: If the input color format is invalid.
        """
        if isinstance(color, str) and color.startswith("#") and len(color) in {4, 7}:
            return color  # Valid hex color
        elif isinstance(color, tuple) and len(color) == 3 and all(0 <= c <= 255 for c in color):
            return self.rgb_to_hex(color)  # Convert RGB to hex
        else:
            raise ValueError("Invalid color format. Use hex ('#RRGGBB' or '#RGB') or RGB tuple (e.g., (255, 255, 255)).")

    # Static method to convert RGB to hex
    @staticmethod
    def rgb_to_hex(rgb: Tuple[int, int, int]) -> str:
        """
        Convert an RGB tuple to a hex color string.

        Args:
            rgb (Tuple[int, int, int]): RGB color values (0-255).

        Returns:
            str: A hex color string in the format '#RRGGBB'.
        """
        return "#{:02x}{:02x}{:02x}".format(*rgb)

    # Static method to convert hex to RGB
    @staticmethod
    def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
        """
        Convert a hex color string to an RGB tuple.

        Args:
            hex_color (str): A hex color string in the format '#RRGGBB' or '#RGB'.

        Returns:
            Tuple[int, int, int]: RGB color values (0-255).

        Raises:
            ValueError: If the hex color format is invalid.
        """
        hex_color = hex_color.lstrip("#")
        if len(hex_color) not in {3, 6}:
            raise ValueError("Invalid hex format. Use '#RRGGBB' or '#RGB'.")
        if len(hex_color) == 3:  # Expand shorthand hex (e.g., "#FFF" -> "#FFFFFF")
            hex_color = "".join([c*2 for c in hex_color])
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    # Method to get the color in RGB format
    def as_rgb(self) -> Tuple[int, int, int]:
        """
        Return the color as an RGB tuple.

        Returns:
            Tuple[int, int, int]: RGB color values (0-255).
        """
        return self.hex_to_rgb(self.color)

    # Method to get the color in hex format
    def as_hex(self) -> str:
        """
        Return the color as a hex string.

        Returns:
            str: Hex color string in the format '#RRGGBB'.
        """
        return self.color

    # Represention
    def __repr__(self) -> str:
        """
        Return a string representation of the COLOR instance.

        Returns:
            str: A string in the format "COLOR('#RRGGBB')".
        """
        return f"COLOR('{self.color}')"