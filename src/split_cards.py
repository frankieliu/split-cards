#!/usr/bin/env python3
"""
Script to split cards.png into 28 individual cards sized at 2.5 x 3.5 inches
"""

from PIL import Image
import os

# Configuration
INPUT_FILE = "resources/cards.png"
OUTPUT_DIR = "output/individual_cards"
NUM_CARDS = 28
DPI = 300  # Standard print DPI

# Target size in inches
TARGET_WIDTH_INCHES = 2.5
TARGET_HEIGHT_INCHES = 3.5

# Convert to pixels at 300 DPI
TARGET_WIDTH_PX = int(TARGET_WIDTH_INCHES * DPI)  # 750 pixels
TARGET_HEIGHT_PX = int(TARGET_HEIGHT_INCHES * DPI)  # 1050 pixels

def main():
    # Load the image
    img = Image.open(INPUT_FILE)
    width, height = img.size

    print(f"Original image size: {width}x{height} pixels")

    # Calculate individual card size from the source image
    card_width = width // NUM_CARDS
    card_height = height

    print(f"Source card size: {card_width}x{card_height} pixels")
    print(f"Target card size: {TARGET_WIDTH_PX}x{TARGET_HEIGHT_PX} pixels ({TARGET_WIDTH_INCHES}x{TARGET_HEIGHT_INCHES} inches at {DPI} DPI)")

    # Create output directory if it doesn't exist
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Split and save each card
    for i in range(NUM_CARDS):
        # Calculate crop box for this card
        left = i * card_width
        top = 0
        right = left + card_width
        bottom = card_height

        # Crop the card
        card = img.crop((left, top, right, bottom))

        # Scale to target size (2.5 x 3.5 inches at 300 DPI)
        card_resized = card.resize((TARGET_WIDTH_PX, TARGET_HEIGHT_PX), Image.Resampling.LANCZOS)

        # Save with DPI metadata for proper printing
        output_filename = os.path.join(OUTPUT_DIR, f"card_{i+1:02d}.png")
        card_resized.save(output_filename, dpi=(DPI, DPI))

        print(f"Saved: {output_filename}")

    print(f"\nSuccessfully split {NUM_CARDS} cards into {OUTPUT_DIR}/")

if __name__ == "__main__":
    main()
