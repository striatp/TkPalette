import tkinter as tk
from tkpalette import Palette, PaletteColorPicker, BasicColorPicker

def main():
    root = tk.Tk()
    root.title("Color Picker Example")

    # Initialize Palette class
    palettes = Palette()

    # Initialize and display Basic Color Picker
    basic_picker = BasicColorPicker(root)

    # Initialize and display Palette Color Picker
    palette_picker = PaletteColorPicker(root, palettes)

    root.mainloop()

if __name__ == "__main__":
    main()