# Digitized English Textbook Project Starter Template

This pre-configured template contains the complete engine, UI components, static bundler, local dev server, and deployment setup for converting any English textbook into an interactive digital web app.

---

## Project Structure

```
template_project/
├── assets/                  # Put your new textbook PDF / raw materials here
├── builder/
│   ├── assembler.py         # Python document compiler
│   ├── styles/main.css      # Responsive CSS design system
│   └── templates/           # HTML templates (base.html, content.html)
├── pdf_structure.json       # Content data model (Units, pages, vocab, dialogues)
├── quiz_data.json          # Interactive quiz datasets
├── build_app.py             # App build trigger (python build_app.py)
├── scripts/build_dist.js    # Production bundler (npm run build -> dist/)
├── server.js                # High-performance local dev server with audio range streaming
├── vercel.json              # Zero-config Vercel deployment setup
└── package.json             # NPM dependencies & scripts
```

---

## 🚀 Quick Start Guide

### 1. Copy Template to your New Book Folder
Copy this `template_project/` directory to your target workspace (e.g. `e:\Projects\ChinaTextBook\English\Grade2_Volume1`).

### 2. Add New Book Assets
Drop your new English textbook PDF or audio files into the `assets/` folder.

### 3. Build & Run
```bash
# Compile HTML App
python build_app.py

# Start Local Dev Server
node server.js

# Deploy to Vercel
npx vercel --prod
```
