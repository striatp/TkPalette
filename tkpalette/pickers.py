import tkinter as tk
from tkinter import colorchooser
from .colors import COLOR # Assuming the COLOR class is in colors.py
from .presets import Palette # Assuming the Palette class is in presets.py

class BasicColorPicker:
    """
    A simple color picker to choose any color via hex or RGB input.
    """
    def __init__(self, master: tk.Tk) -> None:
        """
        Initialize the BasicColorPicker with a Tkinter window.
        
        Args:
            master (tk.Tk): The parent Tkinter window.
        """
        self.master = master
        self.selected_color = COLOR("#FFFFFF")  # Default color (white)
        
        # Create a button to open the color chooser dialog
        self.color_button = tk.Button(master, text="Pick a Color", command=self.pick_color)
        self.color_button.pack(pady=10)

        # Display the selected color
        self.color_display = tk.Label(master, text="Selected Color", bg=self.selected_color.as_hex(), width=20)
        self.color_display.pack(pady=10)

    def pick_color(self) -> None:
        """
        Open the color picker dialog and update the selected color.
        """
        color_code = colorchooser.askcolor()[1]  # Ask color dialog returns a tuple (rgb, hex)
        if color_code:  # If the user selects a color
            self.selected_color = COLOR(color_code)  # Update selected color
            self.color_display.config(bg=self.selected_color.as_hex())  # Update the display

class PaletteColorPicker:
    """
    A color picker that lets users pick a color from predefined palettes.
    """
    def __init__(self, master: tk.Tk, palettes: Palette) -> None:
        """
        Initialize the PaletteColorPicker with a Tkinter window and predefined palettes.
        
        Args:
            master (tk.Tk): The parent Tkinter window.
            palettes (Palette): An instance of the Palette class with predefined color themes.
        """
        self.master = master
        self.palettes = palettes  # Store reference to predefined palettes
        self.selected_color = COLOR("#FFFFFF")  # Default color (white)
        
        # Dropdown to select a palette
        self.palette_label = tk.Label(master, text="Select Palette:")
        self.palette_label.pack(pady=10)
        
        self.palette_menu = tk.OptionMenu(master, tk.StringVar(value="Warm"), *self.palettes.list_palettes())
        self.palette_menu.pack(pady=10)
        
        # Button to open palette color picker
        self.palette_button = tk.Button(master, text="Pick Color from Palette", command=self.pick_palette_color)
        self.palette_button.pack(pady=10)
        
        # Display the selected color
        self.color_display = tk.Label(master, text="Selected Color", bg=self.selected_color.as_hex(), width=20)
        self.color_display.pack(pady=10)

    def pick_palette_color(self) -> None:
        """
        Open the palette picker to choose a color from the selected palette.
        """
        # Get selected palette name from the dropdown
        selected_palette_name = self.palette_menu.get()
        selected_palette = self.palettes.get_palette(selected_palette_name)
        
        # Create a new window for palette selection
        self.palette_window = tk.Toplevel(self.master)
        self.palette_window.title(f"Pick Color from {selected_palette_name}")
        
        for color_name, color in selected_palette.items():
            color_button = tk.Button(self.palette_window, text=color_name, bg=color.as_hex(), width=20,
                                     command=lambda color=color: self.select_color_from_palette(color))
            color_button.pack(pady=5)

    def select_color_from_palette(self, color: COLOR) -> None:
        """
        Set the selected color from the palette to the display.
        
        Args:
            color (COLOR): The color selected from the palette.
        """
        self.selected_color = color  # Update the selected color
        self.color_display.config(bg=self.selected_color.as_hex())  # Update the display
        self.palette_window.destroy()  # Close the palette window