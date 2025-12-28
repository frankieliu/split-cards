#!/usr/bin/env python3
"""
Script to create 3x3 collages of cards at 7.5 x 10.5 inches
"""

from PIL import Image
import os

# Configuration
INPUT_DIR = "output/individual_cards"
OUTPUT_DIR = "output/collages"
DPI = 300

# Collage size in inches
COLLAGE_WIDTH_INCHES = 7.5
COLLAGE_HEIGHT_INCHES = 10.5

# Convert to pixels at 300 DPI
COLLAGE_WIDTH_PX = int(COLLAGE_WIDTH_INCHES * DPI)  # 2250 pixels
COLLAGE_HEIGHT_PX = int(COLLAGE_HEIGHT_INCHES * DPI)  # 3150 pixels

# 3x3 grid
GRID_COLS = 3
GRID_ROWS = 3

# Each card slot size (should be 750x1050, matching our individual cards)
CARD_WIDTH = COLLAGE_WIDTH_PX // GRID_COLS  # 750 pixels
CARD_HEIGHT = COLLAGE_HEIGHT_PX // GRID_ROWS  # 1050 pixels

def create_collage(card_numbers, output_filename):
    """
    Create a 3x3 collage from the given card numbers.

    Args:
        card_numbers: List of 9 card numbers (1-28)
        output_filename: Output filename for the collage
    """
    # Create a new blank image
    collage = Image.new('RGB', (COLLAGE_WIDTH_PX, COLLAGE_HEIGHT_PX), 'white')

    # Place each card in the grid
    for idx, card_num in enumerate(card_numbers):
        row = idx // GRID_COLS
        col = idx % GRID_COLS

        # Load the card image
        card_filename = os.path.join(INPUT_DIR, f"card_{card_num:02d}.png")
        card_img = Image.open(card_filename)

        # Calculate position
        x = col * CARD_WIDTH
        y = row * CARD_HEIGHT

        # Paste the card into the collage
        collage.paste(card_img, (x, y))

        print(f"  Placed card_{card_num:02d} at position ({col}, {row})")

    # Save the collage with DPI metadata
    collage.save(output_filename, dpi=(DPI, DPI))
    print(f"Saved: {output_filename}\n")

def main():
    print(f"Creating collages at {COLLAGE_WIDTH_INCHES}x{COLLAGE_HEIGHT_INCHES} inches ({COLLAGE_WIDTH_PX}x{COLLAGE_HEIGHT_PX} pixels)")
    print(f"Each card slot: {CARD_WIDTH}x{CARD_HEIGHT} pixels\n")

    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Collage 1: card_01 repeated 9 times
    print("Creating collage 1: card_01 repeated 9 times")
    create_collage([1] * 9, os.path.join(OUTPUT_DIR, "collage_1.png"))

    # Collage 2: cards 02-10
    print("Creating collage 2: cards 02-10")
    create_collage(list(range(2, 11)), os.path.join(OUTPUT_DIR, "collage_2.png"))

    # Collage 3: cards 11-19
    print("Creating collage 3: cards 11-19")
    create_collage(list(range(11, 20)), os.path.join(OUTPUT_DIR, "collage_3.png"))

    # Collage 4: cards 20-28
    print("Creating collage 4: cards 20-28")
    create_collage(list(range(20, 29)), os.path.join(OUTPUT_DIR, "collage_4.png"))

    print("Successfully created 4 collages in output/collages/")

if __name__ == "__main__":
    main()
