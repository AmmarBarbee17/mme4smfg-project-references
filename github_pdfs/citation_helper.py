"""
Auto-generated helper for finding correct PDF file and page
"""
import json
from pathlib import Path

FILE_MAPPING = {
  "Alebrahim2025": {
    "type": "single",
    "filename": "Alebrahim2025.pdf",
    "pages": 20
  },
  "Bhandari2025": {
    "type": "split",
    "chunks": [
      {
        "filename": "Bhandari2025_part1.pdf",
        "pages": [
          1,
          2,
          3,
          4,
          5,
          6,
          7,
          8,
          9,
          10,
          11,
          12,
          13,
          14,
          15,
          16,
          17,
          18,
          19,
          20,
          21,
          22,
          23,
          24,
          25,
          26,
          27,
          28,
          29,
          30,
          31
        ],
        "start_page": 1,
        "end_page": 31
      },
      {
        "filename": "Bhandari2025_part2.pdf",
        "pages": [
          32,
          33,
          34,
          35,
          36,
          37,
          38,
          39,
          40,
          41,
          42,
          43,
          44,
          45,
          46,
          47
        ],
        "start_page": 32,
        "end_page": 47
      },
      {
        "filename": "Bhandari2025_part3.pdf",
        "pages": [
          48,
          49,
          50,
          51,
          52,
          53,
          54,
          55,
          56,
          57,
          58,
          59,
          60,
          61,
          62,
          63,
          64,
          65,
          66,
          67,
          68,
          69,
          70
        ],
        "start_page": 48,
        "end_page": 70
      },
      {
        "filename": "Bhandari2025_part4.pdf",
        "pages": [
          71,
          72,
          73,
          74,
          75,
          76,
          77,
          78
        ],
        "start_page": 71,
        "end_page": 78
      }
    ],
    "total_pages": 78
  },
  "Costa2016": {
    "type": "single",
    "filename": "Costa2016.pdf",
    "pages": 11
  },
  "Dong2022": {
    "type": "single",
    "filename": "Dong2022.pdf",
    "pages": 21
  },
  "Du2020": {
    "type": "single",
    "filename": "Du2020.pdf",
    "pages": 19
  },
  "Grossin2021": {
    "type": "single",
    "filename": "Grossin2021.pdf",
    "pages": 21
  },
  "Gupta2023": {
    "type": "single",
    "filename": "Gupta2023.pdf",
    "pages": 5
  },
  "Hu2018": {
    "type": "single",
    "filename": "Hu2018.pdf",
    "pages": 14
  },
  "Pfeiffer2021": {
    "type": "single",
    "filename": "Pfeiffer2021.pdf",
    "pages": 28
  },
  "Rasaki2021": {
    "type": "single",
    "filename": "Rasaki2021.pdf",
    "pages": 30
  },
  "Ruscitti2020": {
    "type": "single",
    "filename": "Ruscitti2020.pdf",
    "pages": 14
  },
  "Spina2024": {
    "type": "single",
    "filename": "Spina2024.pdf",
    "pages": 24
  },
  "Wang2019": {
    "type": "single",
    "filename": "Wang2019.pdf",
    "pages": 22
  },
  "Zhang2020": {
    "type": "single",
    "filename": "Zhang2020.pdf",
    "pages": 20
  },
  "Zhao2024": {
    "type": "single",
    "filename": "Zhao2024.pdf",
    "pages": 20
  }
}

def get_pdf_url(citation_key, page_number):
    """
    Get the GitHub URL for a specific citation and page
    
    Args:
        citation_key: e.g., "Gupta2023"
        page_number: Page number within that citation (1-indexed)
    
    Returns:
        tuple: (filename, absolute_page_in_that_file)
    """
    if citation_key not in FILE_MAPPING:
        return None, None
    
    info = FILE_MAPPING[citation_key]
    
    if info['type'] == 'single':
        return info['filename'], page_number
    else:
        # Find which chunk contains this page
        for chunk in info['chunks']:
            if chunk['start_page'] <= page_number <= chunk['end_page']:
                # Calculate page within this chunk
                page_in_chunk = page_number - chunk['start_page'] + 1
                return chunk['filename'], page_in_chunk
        
        return None, None

def generate_url(citation_key, page_number, base_url="github_pdfs"):
    """Generate full URL with fragment identifier"""
    filename, page = get_pdf_url(citation_key, page_number)
    if filename:
        return f"{{base_url}}/{{filename}}#page={{page}}"
    return None
