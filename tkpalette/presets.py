from typing import Dict, List
from colors import COLOR # Import the COLOR class

class Palette:
    """
    A collection of predefined color palettes for quick access.

    Attributes:
        palettes (Dict[str, Dict[str, COLOR]]): Dictionary of palettes with their color names and COLOR instances.
    """
    palettes: Dict[str, Dict[str, COLOR]] = {}

    # Initialisation
    def __init__(self) -> None:
        """
        Initialize the Palette class and load predefined palettes.
        """
        self.palettes = self._load_presets()

    # Method to load predefined palettes
    def _load_presets(self) -> Dict[str, Dict[str, COLOR]]:
        """
        Define and return a dictionary of predefined color palettes.

        Returns:
            Dict[str, Dict[str, COLOR]]: Predefined palettes with theme names and colors.
        """
        return {
            "Warm": {
                "sunset": COLOR("#FF5733"),
                "orange": COLOR("#FF6F00"),
                "gold": COLOR("#FFC300"),
                "chocolate": COLOR("#D2691E"),
            },
            "Cool": {
                "ice": COLOR("#A0E6FF"),
                "ocean": COLOR("#0077BE"),
                "navy": COLOR("#001F3F"),
                "midnight": COLOR("#2C3E50"),
            },
            "Nature": {
                "forest": COLOR("#2E8B57"),
                "moss": COLOR("#6B8E23"),
                "soil": COLOR("#8B4513"),
                "sky": COLOR("#87CEEB"),
            },
            "Pastel": {
                "baby_blue": COLOR("#B3CDE0"),
                "lavender": COLOR("#C9A0DC"),
                "peach": COLOR("#FFDAB9"),
                "mint": COLOR("#98FF98"),
            },
        }

    # Methos to get a palette
    def get_palette(self, name: str) -> Dict[str, COLOR]:
        """
        Retrieve a color palette by name.

        Args:
            name (str): The name of the palette (e.g., "Warm", "Cool").

        Returns:
            Dict[str, COLOR]: A dictionary of color names and COLOR instances.

        Raises:
            ValueError: If the palette name does not exist.
        """
        if name not in self.palettes:
            raise ValueError(f"Palette '{name}' does not exist.")
        return self.palettes[name]

    # Method to list all palettes
    def list_palettes(self) -> List[str]:
        """
        List all available palette names.

        Returns:
            List[str]: Names of predefined color palettes.
        """
        return list(self.palettes.keys())

    # Representation
    def __repr__(self) -> str:
        """
        Return a string representation of available palettes.

        Returns:
            str: List of palette names.
        """
        return f"Available palettes: {', '.join(self.list_palettes())}"