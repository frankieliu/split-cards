# Card Splitting and PDF Generation

This project contains scripts to process game cards from a single strip image into printable PDFs with cutting lines.

## Project Structure

```
.
├── resources/              # Input files
│   └── cards.png          # Original horizontal strip (28 cards)
├── src/                   # Python scripts
│   ├── split_cards.py
│   ├── create_collages.py
│   ├── create_pdfs.py
│   └── combine_pdfs.py
├── output/                # Generated files
│   ├── individual_cards/  # Step 1 output
│   ├── collages/         # Step 2 output
│   └── pdfs/             # Steps 3 & 4 output
├── pyproject.toml        # Project dependencies
└── README.md             # This file
```

## Overview

The process takes a single horizontal strip of 28 cards and creates print-ready PDFs:

1. **Split** the strip into 28 individual cards (2.5 x 3.5 inches each)
2. **Collage** the cards into four 3x3 grids (7.5 x 10.5 inches each)
3. **Generate PDFs** with cutting lines on letter-sized pages
4. **Combine** all PDFs into a single multi-page document

## Prerequisites

Install dependencies using uv:

```bash
uv sync
```

Or using pip:

```bash
pip install pillow reportlab pypdf
```

## Input

- `resources/cards.png` - A horizontal strip containing 28 cards (8400 x 420 pixels)

## Step 1: Split Cards

Split the original image into 28 individual cards, each sized at 2.5 x 3.5 inches (750 x 1050 pixels at 300 DPI).

```bash
uv run src/split_cards.py
```

**Output:**
- Creates `output/individual_cards/` directory
- Generates `card_01.png` through `card_28.png`
- Each card is 750 x 1050 pixels at 300 DPI

## Step 2: Create Collages

Arrange the cards into four 3x3 grids (7.5 x 10.5 inches each):

- **Collage 1**: card_01 repeated 9 times
- **Collage 2**: cards 02-10
- **Collage 3**: cards 11-19
- **Collage 4**: cards 20-28

```bash
uv run src/create_collages.py
```

**Output:**
- Creates `output/collages/` directory
- Generates `collage_1.png` through `collage_4.png`
- Each collage is 2250 x 3150 pixels (7.5 x 10.5 inches at 300 DPI)

## Step 3: Generate PDFs with Cutting Lines

Create PDFs on letter-sized pages (8.5 x 11 inches) with cutting lines:

```bash
uv run src/create_pdfs.py
```

**Output:**
- Creates `output/pdfs/` directory
- Generates `collage_1.pdf` through `collage_4.pdf`
- Each PDF contains:
  - One collage centered with margins (0.5" left/right, 0.25" top/bottom)
  - 4 vertical cutting lines at card boundaries
  - 4 horizontal cutting lines at card boundaries
  - All lines extend to paper edge

## Step 4: Combine PDFs

Merge all four PDFs into a single multi-page document:

```bash
uv run src/combine_pdfs.py
```

**Output:**
- Creates `output/pdfs/all_collages.pdf`
- Contains 4 pages (one for each collage)

## Complete Workflow

Run all steps in sequence:

```bash
uv run src/split_cards.py
uv run src/create_collages.py
uv run src/create_pdfs.py
uv run src/combine_pdfs.py
```

## Specifications

### Card Dimensions
- Individual cards: 2.5 x 3.5 inches (750 x 1050 pixels at 300 DPI)

### Collage Dimensions
- 3x3 grid: 7.5 x 10.5 inches (2250 x 3150 pixels at 300 DPI)

### PDF Page Dimensions
- Page size: Letter (8.5 x 11 inches)
- Margins: 0.5" left/right, 0.25" top/bottom
- Collage: 7.5 x 10.5 inches (not rescaled)

### Cutting Lines
- 4 vertical lines at: 0.5", 3.0", 5.5", 8.0"
- 4 horizontal lines at: 0.25", 3.75", 7.25", 10.75"
- All lines extend to paper edge for easy trimming

## Notes

- All images maintain 300 DPI for high-quality printing
- No resolution is lost during the process
- Cards fit perfectly into the 3x3 grid without scaling
- The collage fits perfectly on letter-sized paper with specified margins

