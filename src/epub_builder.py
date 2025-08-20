from ebooklib import epub

def setup_book_metadata(book, title, author):
    """设置EPUB书籍的元数据"""
    book.set_title(title)
    book.set_language('zh')
    book.add_author(author)

def add_cover_image(book, cover_image):
    """添加封面图片"""
    if not cover_image:
        return
    
    try:
        with open(cover_image, 'rb') as cover:
            book.set_cover("cover.jpg", cover.read())
    except Exception as e:
        print(f"无法读取封面图片: {e}")

def create_chapter_items(book, chapters):
    """创建章节项目并添加到书籍中"""
    for i, chapter in enumerate(chapters):
        # 提取章节标题和内容
        lines = chapter.split('\n')
        chapter_title = lines[0] if lines else f'第{i + 1}章'
        
        # 获取章节内容（排除标题行）
        chapter_content = '\n'.join(lines[1:]) if len(lines) > 1 else ''
        
        # 将换行符替换为两个<br>标签，以保持段落之间的空行
        formatted_content = chapter_content.replace('\n', '<br><br>') if chapter_content else ''

        chapter_item = epub.EpubHtml(title=chapter_title, file_name=f'chapter_{i + 1}.xhtml', lang='zh')
        chapter_item.set_content(f'<h1>{chapter_title}</h1><p>{formatted_content}</p>')
        book.add_item(chapter_item)
        book.spine.append(chapter_item)

def save_epub_file(book, title):
    """保存EPUB文件"""
    output_filename = f"{title}.epub"
    
    try:
        epub.write_epub(output_filename, book)
        print(f"EPUB文件已保存: {output_filename}")
        return True
    except Exception as e:
        print(f"无法保存EPUB文件: {e}")
        return False

def create_epub_book(chapters, title, author, cover_image=None):
    """创建EPUB书籍对象"""
    # 创建EPUB对象
    book = epub.EpubBook()
    
    # 设置元数据
    setup_book_metadata(book, title, author)
    
    # 添加封面
    add_cover_image(book, cover_image)
    
    # 创建章节项目
    create_chapter_items(book, chapters)
    
    # 添加导航
    book.add_item(epub.EpubNav())
    
    return book 