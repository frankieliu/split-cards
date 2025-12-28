#!/usr/bin/env python3
"""
Script to combine 4 individual PDFs into one multi-page PDF
"""

from pypdf import PdfWriter, PdfReader
import os

# Configuration
PDF_DIR = "output/pdfs"
OUTPUT_FILE = os.path.join(PDF_DIR, "all_collages.pdf")

def main():
    # Create PDF writer
    writer = PdfWriter()

    print("Combining PDFs into single file...")

    # Add each PDF in order
    for i in range(1, 5):
        pdf_file = os.path.join(PDF_DIR, f"collage_{i}.pdf")
        print(f"  Adding {pdf_file}")

        # Read the PDF and add its pages
        reader = PdfReader(pdf_file)
        for page in reader.pages:
            writer.add_page(page)

    # Write out the merged PDF
    with open(OUTPUT_FILE, "wb") as output:
        writer.write(output)

    print(f"\nSuccessfully created: {OUTPUT_FILE}")
    print("Contains 4 pages (collages 1-4)")

if __name__ == "__main__":
    main()
