import os
import json
import fitz # PyMuPDF
from PIL import Image

def extract_pdf_assets():
    pdf_path = os.path.join("assets", "义务教育教科书·英语（一年级起点）一年级下册.pdf")
    output_dir = os.path.join("images", "pages")
    os.makedirs(output_dir, exist_ok=True)

    print(f"Opening PDF: {pdf_path}")
    doc = fitz.open(pdf_path)
    total_pages = len(doc)
    print(f"Total pages: {total_pages}")

    manifest_pages = []

    for idx, page in enumerate(doc):
        page_num = idx + 1
        filename = f"page_{page_num:02d}.webp"
        filepath = os.path.join(output_dir, filename)

        # Render page to image at 2.0x resolution for sharp display
        zoom = 2.0
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat)
        
        # Save as WebP
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        img.save(filepath, "WEBP", quality=85)

        manifest_pages.append({
            "page": page_num,
            "filename": filename,
            "path": f"images/pages/{filename}",
            "width": pix.width,
            "height": pix.height
        })

        # Print out text extracted from page for structure inspection
        text = page.get_text()
        if text.strip():
            print(f"--- Page {page_num} Text ---")
            print(text.strip()[:200])

    manifest_path = os.path.join("images", "pages_manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump({
            "total_pages": total_pages,
            "pages": manifest_pages
        }, f, ensure_ascii=False, indent=2)

    print(f"\nExtraction complete! Saved {total_pages} page WebP images to {output_dir} and manifest to {manifest_path}")

if __name__ == "__main__":
    extract_pdf_assets()
