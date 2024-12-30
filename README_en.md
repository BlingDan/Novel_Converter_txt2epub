# 📖 Novel Converter

## ✨ Introduction
Welcome to the Novel Converter! This Python script allows you to easily convert TXT format novels into EPUB format, supporting chapter division and cover addition. Whether you want to publish your own novel as an e-book or convert a favorite novel into a more readable format, this tool can meet your needs.

## 📦 Dependencies
Before you start, make sure to install the `EbookLib` library. You can install it using the following command:
```bash
pip install EbookLib
```

## 🛠️ Usage
1. **Prepare Files**:
   - Name your novel text file as `novel.txt` and the cover image as `cover.jpg`, placing them in the same directory as the script.
   - Ensure that there are two newline characters between chapters in the TXT file for the program to correctly identify chapters.

2. **Configure Environment Variables**:
   - Create a file named `.env` with the following content:
     ```env
     TXT_FILE=./novel.txt
     COVER_IMAGE=./cover.jpg
     TITLE=Your Novel Title
     AUTHOR=Author Name
     ```

3. **Run the Script**:
   - Execute the following command in the terminal:
   ```bash
   python src/main.py
   ```

4. **Output File**:
   - After conversion, the output EPUB file will be named according to the title specified in the `.env` file, for example, `Your Novel Title.epub`.

## ⚠️ Notes
- Ensure that there are two newline characters between chapters in the TXT file for the program to correctly identify chapters.
- The cover image should be in JPEG format and named `cover.jpg`.

## 📖 Example
In `src/main.py`, the example call is as follows:
```python
create_epub('novel.txt', 'cover.jpg', 'Your Novel Title', 'Author Name')
```
You can modify the title and author name as needed.

## 💬 Feedback & Support
If you encounter any issues while using this tool, feel free to provide feedback! I will respond as soon as possible.

Thank you for using this tool, and happy writing! 🎉