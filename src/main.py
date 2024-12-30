import os
from dotenv import load_dotenv
from ebooklib import epub
import chardet

# 加载环境变量
load_dotenv()

def create_epub(txt_file, cover_image, title, author):
    # 创建EPUB对象
    book = epub.EpubBook()

    # 设置元数据
    book.set_title(title)
    book.set_language('zh')
    book.add_author(author)

    # 添加封面
    if cover_image:
        try:
            with open(cover_image, 'rb') as cover:
                book.set_cover("cover.jpg", cover.read())
        except Exception as e:
            print(f"无法读取封面图片: {e}")
            return

    # 读取TXT文件并识别章节
    try:
        with open(txt_file, 'rb') as f:  # 以二进制模式读取
            raw_data = f.read()
            result = chardet.detect(raw_data)  # 检测编码
            encoding = result['encoding']  # 获取检测到的编码

        with open(txt_file, 'r', encoding=encoding, errors='ignore') as f:  # 使用检测到的编码，忽略错误
            chapters = []
            chapter = []
            for line in f:
                if line.strip():  # 非空行
                    if line.startswith("第") and "章" in line:  # 检查是否为章节标题
                        if chapter:  # 如果当前章节不为空，保存当前章节
                            chapters.append('\n'.join(chapter))
                            chapter = []
                    chapter.append(line.strip())
                else:  # 空行，表示章节结束
                    if chapter:
                        chapters.append('\n'.join(chapter))
                        chapter = []
            if chapter:  # 添加最后一章
                chapters.append('\n'.join(chapter))
    except Exception as e:
        print(f"无法读取小说文件: {e}")
        return

    # 添加章节到EPUB
    for i, chapter in enumerate(chapters):
        # 将换行符替换为两个<br>标签，以保持段落之间的空行
        formatted_chapter = chapter.replace('\n', '<br><br>')  # 每个段落之间空一行
        
        # 提取章节标题
        lines = chapter.split('\n')
        chapter_title = lines[0] if lines else f'第{i + 1}章'  # 使用章节内容的第一行作为标题

        chapter_item = epub.EpubHtml(title=chapter_title, file_name=f'chapter_{i + 1}.xhtml', lang='zh')
        chapter_item.set_content(f'<h1>{chapter_title}</h1><p>{formatted_chapter}</p>')
        book.add_item(chapter_item)
        book.spine.append(chapter_item)

    # 添加导航
    book.add_item(epub.EpubNav())

    # 从环境变量获取标题作为文件名
    output_filename = f"{title}.epub"

    # 保存EPUB文件
    try:
        epub.write_epub(output_filename, book)
    except Exception as e:
        print(f"无法保存EPUB文件: {e}")

if __name__ == "__main__":
    # 从环境变量获取参数
    txt_file = os.getenv('TXT_FILE')
    cover_image = os.getenv('COVER_IMAGE')
    title = os.getenv('TITLE')
    author = os.getenv('AUTHOR')

    create_epub(txt_file, cover_image, title, author) 