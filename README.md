# Organize Downloads Folder

Automatically organize your cluttered Downloads folder! This Python script sorts files into categorized subfolders (Images, Documents, Archives, etc.) based on file type—keeping your files tidy and easy to find.

## ✨ Features

- 🗂️ **Auto-sorts files** by type (Images, Videos, Documents, Code, etc.)
- 📁 **23+ file categories** covering most common file types
- 🔧 **Zero configuration needed** – just run it
- 💻 **Cross-platform** – works on Windows, macOS, and Linux
- 🛡️ **Safe handling** – skips existing folders and handles errors gracefully

## 🚀 Quick Start

### Prerequisites
- **Python 3.6+** installed on your computer ([download here](https://www.python.org/downloads/))

### Setup & Run

1. **Clone or download** this repository:
   ```bash
   git clone https://github.com/recklessrashdan/organize_downloads_folder.git
   cd organize_downloads_folder
   ```

2. **Run the script:**
   ```bash
   python organize_downloads.py
   ```

   That's it! The script will organize your Downloads folder automatically.

## 📂 File Categories

Files are sorted into the following folders:

| Category | File Types |
|----------|-----------|
| **Images** | jpg, jpeg, png, gif, bmp, tiff, webp, heic |
| **Videos** | mp4, mkv, flv, avi, mov, wmv, webm |
| **Documents** | pdf, doc, docx, txt, xls, xlsx, ppt, pptx, odt, ods, odp, rtf |
| **Audio** | mp3, wav, aac, flac, ogg, wma |
| **Archives** | zip, rar, 7z, tar, gz, bz2, xz |
| **Code** | py, js, html, css, java, c, cpp, json, xml, sh |
| **Executables** | exe, msi, dmg, app, deb, rpm |
| **Fonts** | ttf, otf, woff, woff2 |
| **Others** | Any files that don't match above categories |

**And more:** Spreadsheets, Presentations, Disk Images, Torrents, Virtual Machines, CAD Files, Ebooks, and more!

## 📖 How It Works

1. Script reads your Downloads folder
2. Creates category folders (if they don't exist yet)
3. Moves each file into its matching category folder
4. Prints a summary of what was moved
5. Unmatched files go into an "Others" folder

## ⚙️ Customization

To organize a different folder (not your Downloads), edit the script:

```python
# At the bottom of organize_downloads.py, change the path:
if __name__ == "__main__":
    downloads_path = os.path.expanduser("~/Downloads")  # Change this path
    organize_downloads(downloads_path)
```

## 🆘 Troubleshooting

**"Python not found"**
- Ensure Python is installed and added to your PATH
- Try `python3` instead of `python`

**"Permission denied" errors**
- Run the script with administrator/sudo privileges
- Or change the folder path to one you have write access to

**Files didn't move**
- Check the console output for specific error messages
- Ensure you have read/write permissions for the Downloads folder

## 💡 Tips

- **Backup first:** Consider backing up your Downloads folder before running for the first time
- **Run regularly:** Schedule this script to run weekly to keep things tidy
- **Add custom rules:** Modify the `file_categories` dictionary to add more file types or categories

## 📝 License & Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve the script.

---

**Questions?** Check the troubleshooting section above or open an issue on GitHub.
