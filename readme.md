# File Rename

This simple Python script helps you batch rename image files in a folder. It sorts the images by name and renames them to a numerical sequence (1, 2, 3...), while preserving the original file extensions.

## Features

- Automatically detects and renames image files in the current folder
- Supports .png, .jpg, .jpeg, .gif, .bmp .webp formats
- Sorts files by original filename before renaming
- Avoids filename conflicts by automatically handling duplicate filenames
- Can be packaged as a standalone Windows executable (.exe)

## Usage

### Running as a Python script

1. Ensure you have Python 3 installed on your system
2. Download `rename_images.py` to the directory containing the images you want to rename
3. Open a command prompt or terminal and navigate to that directory
4. Run the following command:
```bash
python rename_images.py
```

### Running as a Windows executable

1. Download the packaged `rename_images.exe`
2. Place `rename_images.exe` in the directory containing the images you want to rename
3. Double-click to run `rename_images.exe`

## Notes

- Please backup important files before use, to prevent accidental loss
- The script renames files directly; this operation is irreversible
- If numerically named files already exist in the directory, the script will automatically add suffixes (like 1_1, 2_1, etc.) to avoid conflicts
