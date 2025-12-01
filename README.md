# GitHub PDF Hosting Setup

This system prepares reference PDFs for GitHub hosting with the 25MB file size limit.

## What It Does

1. **Splits large PDFs** (>25MB) into smaller chunks
2. **Creates individual citation links** directly to each reference PDF
3. **Handles split files automatically** - links to the correct part + page

## Generated Files

- `github_pdfs/` - Folder with all PDFs ready for GitHub upload
  - Single files for PDFs < 25MB (e.g., `Gupta2023.pdf`)
  - Split files for large PDFs (e.g., `Bhandari2025_part1.pdf`, `Bhandari2025_part2.pdf`, etc.)
- `citation_urls.tex` - LaTeX macros for citation URLs
- `github_pdfs/file_mapping.json` - Mapping of citations to their files
- `github_pdfs/citation_helper.py` - Python helper for URL generation

## How Citations Work

### In presentation.tex:

```latex
\pdfref{Gupta2023}{2}{Layer-by-layer UV curing}
```

### Becomes a link to:

- **Small PDFs**: `github_pdfs/Gupta2023.pdf#page=2`
- **Split PDFs**: Automatically routes to correct part
  - `\pdfref{Bhandari2025}{35}{text}` → `github_pdfs/Bhandari2025_part2.pdf#page=4`
  - (Page 35 is in part 2, which starts at page 32, so page 35-31=4 in that part)

## For GitHub Pages Hosting

1. **Upload to your repository:**
   ```
   your-repo/
   ├── presentation.pdf
   └── github_pdfs/
       ├── Alebrahim2025.pdf
       ├── Bhandari2025_part1.pdf
       ├── Bhandari2025_part2.pdf
       ├── ...
       └── file_mapping.json
   ```

2. **Enable GitHub Pages** in repository settings

3. **Access via URLs:**
   - `https://yourusername.github.io/your-repo/presentation.pdf`
   - Citations will automatically link to `github_pdfs/...pdf#page=X`

## File Breakdown

| Citation | Original Size | GitHub Version |
|----------|--------------|----------------|
| Alebrahim2025 | 8.89 MB | Single file |
| Bhandari2025 | 74.25 MB | **Split into 4 parts** (23MB, 23MB, 25MB, 4MB) |
| Costa2016 | 1.35 MB | Single file |
| Dong2022 | 8.08 MB | Single file |
| Du2020 | 1.16 MB | Single file |
| Grossin2021 | 1.72 MB | Single file |
| Gupta2023 | 1.84 MB | Single file |
| Hu2018 | 4.42 MB | Single file |
| Pfeiffer2021 | 14.17 MB | Single file |
| Rasaki2021 | 5.67 MB | Single file |
| Ruscitti2020 | 3.59 MB | Single file |
| Spina2024 | 5.21 MB | Single file |
| Wang2019 | 2.56 MB | Single file |
| Zhang2020 | 5.42 MB | Single file |
| Zhao2024 | 5.91 MB | Single file |

**Total:** 15 citations, 18 PDF files (14 single + 4 parts for Bhandari2025)

## Updating

Run `compile.bat` to regenerate everything if you add/update reference PDFs.
