from config import Config
from chapter_parser import parse_chapters_from_file
from epub_builder import create_epub_book, save_epub_file

def create_epub(txt_file, cover_image, title, author):
    """创建EPUB文件的主函数"""
    # 解析章节
    chapters = parse_chapters_from_file(txt_file)
    if not chapters:
        print("没有检测到任何章节，无法创建EPUB文件")
        return
    
    # 创建EPUB书籍
    book = create_epub_book(chapters, title, author, cover_image)
    
    # 保存文件
    save_epub_file(book, title)

def main():
    """主函数"""
    # 验证配置
    if not Config.validate_config():
        return
    
    # 获取配置参数
    txt_file = Config.get_txt_file()
    cover_image = Config.get_cover_image()
    title = Config.get_title()
    author = Config.get_author()
    
    # 创建EPUB
    create_epub(txt_file, cover_image, title, author)

if __name__ == "__main__":
    main() 