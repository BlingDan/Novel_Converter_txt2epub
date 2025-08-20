"""
Novel Converter - TXT to EPUB Converter
A modular tool for converting TXT novels to EPUB format with intelligent chapter detection and chapter marking features.
"""

__version__ = "1.1.1"
__author__ = "BlingDan"

from .config import Config
from .chapter_parser import parse_chapters_from_file, is_chapter_title
from .epub_builder import create_epub_book, save_epub_file

__all__ = [
    'Config',
    'parse_chapters_from_file',
    'is_chapter_title', 
    'create_epub_book',
    'save_epub_file'
] 