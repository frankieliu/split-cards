#!/usr/bin/env python3
"""
Script to create PDFs with collages and cutting lines on letter-sized pages
"""

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
import os

# Configuration
COLLAGES_DIR = "output/collages"
OUTPUT_DIR = "output/pdfs"

# Page size (letter)
PAGE_WIDTH, PAGE_HEIGHT = letter  # 8.5 x 11 inches

# Margins
LEFT_MARGIN = 0.5 * inch
RIGHT_MARGIN = 0.5 * inch
TOP_MARGIN = 0.25 * inch
BOTTOM_MARGIN = 0.25 * inch

# Collage size
COLLAGE_WIDTH = 7.5 * inch
COLLAGE_HEIGHT = 10.5 * inch

# Grid configuration (3x3)
GRID_COLS = 3
GRID_ROWS = 3

# Card size
CARD_WIDTH = COLLAGE_WIDTH / GRID_COLS  # 2.5 inches
CARD_HEIGHT = COLLAGE_HEIGHT / GRID_ROWS  # 3.5 inches

def create_pdf_with_cutting_lines(collage_num, output_filename):
    """
    Create a PDF with the collage and cutting lines.

    Args:
        collage_num: The collage number (1-4)
        output_filename: Output PDF filename
    """
    # Create canvas
    c = canvas.Canvas(output_filename, pagesize=letter)

    # Input collage image
    collage_image = os.path.join(COLLAGES_DIR, f"collage_{collage_num}.png")

    # Calculate position (bottom-left corner of image in PDF coordinates)
    # PDF coordinates have origin at bottom-left
    x = LEFT_MARGIN
    y = BOTTOM_MARGIN

    # Draw the collage image
    c.drawImage(collage_image, x, y, width=COLLAGE_WIDTH, height=COLLAGE_HEIGHT)

    # Set line style for cutting lines
    c.setStrokeColorRGB(0, 0, 0)  # Black
    c.setLineWidth(0.5)

    # Draw 4 vertical cutting lines (at left, after col1, after col2, right)
    for i in range(4):
        line_x = LEFT_MARGIN + (i * CARD_WIDTH)
        # Extend from top to bottom of page
        c.line(line_x, 0, line_x, PAGE_HEIGHT)
        print(f"  Vertical line {i+1} at x={line_x/inch:.2f} inches")

    # Draw 4 horizontal cutting lines (at bottom, after row1, after row2, top)
    for i in range(4):
        line_y = BOTTOM_MARGIN + (i * CARD_HEIGHT)
        # Extend from left to right of page
        c.line(0, line_y, PAGE_WIDTH, line_y)
        print(f"  Horizontal line {i+1} at y={line_y/inch:.2f} inches")

    # Save the PDF
    c.save()
    print(f"Saved: {output_filename}\n")

def main():
    print(f"Creating PDFs on letter-sized pages ({PAGE_WIDTH/inch}x{PAGE_HEIGHT/inch} inches)")
    print(f"Margins: L/R={LEFT_MARGIN/inch}\", T/B={TOP_MARGIN/inch}\"")
    print(f"Collage size: {COLLAGE_WIDTH/inch}x{COLLAGE_HEIGHT/inch} inches")
    print(f"Card size: {CARD_WIDTH/inch}x{CARD_HEIGHT/inch} inches\n")

    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Create PDFs for all 4 collages
    for i in range(1, 5):
        print(f"Creating PDF for collage {i}")
        output_file = os.path.join(OUTPUT_DIR, f"collage_{i}.pdf")
        create_pdf_with_cutting_lines(i, output_file)

    print("Successfully created 4 PDFs in output/pdfs/")

if __name__ == "__main__":
    main()
