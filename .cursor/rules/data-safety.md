---
description: Enforces data safety rules for this workspace. Always active.
globs: *
---

# Data Safety Rules

## NVIDIA Data — Never Push to GitHub

This workspace uses a personal GitHub repo (watson-the-cat/learning-ai). NVIDIA-specific data must NEVER be committed or pushed to GitHub.

Rules:
- All data files (CSV, XLSX, JSON data, Parquet, etc.) must be listed in .gitignore
- Before any git commit, verify no NVIDIA data files are staged
- If the user adds a new data file, immediately add its pattern to .gitignore
- Scripts and code are fine for GitHub — only data is restricted
- When creating scripts that reference data files, use relative paths and note in the README what data is expected

This rule stays in effect until the user explicitly changes it.
