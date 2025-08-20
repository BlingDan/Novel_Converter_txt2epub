# Novel Converter - TXT to EPUB Converter

欢迎使用小说转换器！这个Python脚本专门为微信读书场景优化，可以轻松地将TXT格式的小说文件转换为EPUB格式，支持章节划分和封面添加，支持多种章节检测方式。生成的EPUB文件完美适配微信读书，提供最佳的阅读体验。无论你是想将自己的小说发布为电子书，还是想将喜欢的小说转换为便于在微信读书中阅读的格式，这个工具都能满足你的需求。

## 📔微信读书效果图

<img src="https://216f8f9.webp.li/2025/08/9ce962418c283913fad30cf3b6920067.png" alt="image-20250820233813880" style="zoom:50%;" />

<img src="https://216f8f9.webp.li/2025/08/19c7cd9e73d3d04f9d076e8fa1593f3b.png" alt="image-20250820233852592" style="zoom:50%;" />

<img src="https://216f8f9.webp.li/2025/08/f9fed99365929e7c3fdc1323b30fc898.png" alt="image-20250820233858748" style="zoom:50%;" />

## ✨ 功能特点

- 🎯 **智能章节检测**：支持多种章节标记格式
- 📚 **灵活配置**：可自定义章节检测策略
- 🔧 **模块化设计**：易于维护和扩展
- 📖 **格式保持**：保持原文段落格式
- 🏷️ **章节标记**：支持自动为章节标题添加特殊字符标记
- ✅ **无重复显示**：章节标题在EPUB中只显示一次，避免重复
- 🎨 **封面支持**：支持自定义封面图片
- 🌍 **编码检测**：自动检测文本文件编码

## 📋 系统要求

- Python 3.7+
- 支持的操作系统：Windows, macOS, Linux

## 🚀 快速开始

### 1. 克隆项目
```bash
git clone git@github.com:BlingDan/Novel_Converter_txt2epub.git
cd Novel_Converter_txt2epub-main
```

### 2. 安装依赖
```bash
pip install -r requirements.txt
```

### 3. 配置环境
复制示例配置文件：
```bash
cp example.env .env
```

编辑 `.env` 文件，设置你的小说文件路径和基本信息。

### 4. 运行转换
```bash
python run.py
```

## 📖 章节检测方式

### 1. 特殊字符标记（推荐）
在章节名前添加特殊字符：
```
#第一章 故事开始
##第二章 情节发展
@第三章 高潮部分
```

### 2. 传统章节格式
支持多种常见格式：
```
第1章 标题
第一章 标题
Chapter 1 标题
1. 标题
一、标题
```

### 3. 双空行分章
使用连续两个空行分隔章节（可配置开关）

### 4. 智能章节标记（新功能）
当识别出章节标题时，可以自动在章节标题前添加特殊字符，使章节标题在EPUB中更加醒目。

**示例：**
原始文本：
```
第一章 故事开始
这是第一章的内容...



第二章 情节发展
这是第二章的内容...
```

启用章节标记后，EPUB中的章节标题会显示为：
```
#第一章 故事开始
#第二章 情节发展
```

## ⚙️ 配置选项

### 环境变量配置

创建 `.env` 文件：

```env
# 基本配置
TXT_FILE=./novels/novel.txt
COVER_IMAGE=./assets/cover.jpg
TITLE=我的小说
AUTHOR=作者名

# 章节检测配置
CHAPTER_DETECTION_METHOD=auto
ENABLE_DOUBLE_EMPTY_LINE=true

# 章节标记功能配置
ENABLE_CHAPTER_MARKER=false
CHAPTER_MARKER=#
```

### 配置说明

| 配置项 | 说明 | 可选值 | 默认值 |
|--------|------|--------|--------|
| `TXT_FILE` | TXT文件路径 | 相对或绝对路径 | `./novels/novel.txt` |
| `COVER_IMAGE` | 封面图片路径 | 相对或绝对路径 | `./assets/cover.jpg` |
| `TITLE` | 书籍标题 | 任意字符串 | 必需 |
| `AUTHOR` | 作者信息 | 任意字符串 | 必需 |
| `CHAPTER_DETECTION_METHOD` | 章节检测方法 | `auto`, `pattern_only`, `double_empty_line_only` | `auto` |
| `ENABLE_DOUBLE_EMPTY_LINE` | 是否启用双空行检测 | `true`, `false` | `true` |
| `ENABLE_CHAPTER_MARKER` | 是否启用章节标记功能 | `true`, `false` | `false` |
| `CHAPTER_MARKER` | 章节标记字符 | `#`, `##`, `@`, `*` 等 | `#` |

## 🎯 使用方法

### 方法一：使用启动脚本（推荐）
```bash
python run.py
```

### 方法二：直接运行模块
```bash
python -m src.main
```

### 方法三：在Python中使用
```python
from src.main import create_epub

create_epub(
    txt_file="./novels/novel.txt",
    cover_image="./assets/cover.jpg",
    title="我的小说",
    author="作者名"
)
```

## 🔍 章节检测策略

### Auto模式（默认）
- 优先使用特殊字符和模式匹配
- 如果启用双空行检测，作为兜底方案
- 如果启用章节标记功能，会在识别出的章节标题前添加特殊字符

### Pattern Only模式
- 仅使用特殊字符和模式匹配
- 不启用双空行检测

### Double Empty Line Only模式
- 仅使用双空行检测
- 适用于没有明确章节标记的文本
- 可以配合章节标记功能使用

## 🏷️ 章节标记功能详解

### 功能说明
当启用章节标记功能时，程序会在识别出章节标题后，自动在章节标题前添加指定的特殊字符。这个标记会出现在最终的EPUB文件中，使章节标题更加醒目。

### 使用场景
1. **统一章节格式**：将所有章节标题都标记为特殊字符格式
2. **提高可读性**：使章节标题在EPUB中更加醒目
3. **美化排版**：让章节标题具有统一的视觉样式

### 配置示例
```env
# 启用章节标记功能，使用 # 作为标记
ENABLE_CHAPTER_MARKER=true
CHAPTER_MARKER=#

# 启用章节标记功能，使用 ## 作为标记
ENABLE_CHAPTER_MARKER=true
CHAPTER_MARKER=##

# 启用章节标记功能，使用 @ 作为标记
ENABLE_CHAPTER_MARKER=true
CHAPTER_MARKER=@
```

### 工作原理
1. **章节识别**：程序识别出章节标题（通过模式匹配或双空行分章）
2. **标记添加**：如果启用了章节标记功能，自动在章节标题前添加特殊字符
3. **EPUB生成**：在最终的EPUB文件中，章节标题显示为带标记的格式，且只显示一次

## 📝 支持的章节格式

### 特殊字符标记
- `#章节标题`
- `##章节标题`
- `@章节标题`

### 数字格式
- `第1章`、`第 1 章`、`第1000章`
- `第1节`、`第 1 节`
- `Chapter 1`、`Chapter 1000`
- `Section 1`、`Section 1000`

### 中文数字格式
- `第一章`、`第一百章`、`第一千章`
- `第一节`、`第一百节`
- `第一部`、`第一百部`

### 其他格式
- `1. 标题`、`1、标题`
- `一、标题`、`一百、标题`

## ⚠️ 章节格式要求与提示

为确保在 EPUB 中正确显示章节标题，请保证每一章的首行即为该章的标题。若使用“双空行分章”，新的章节开始后第一行也应为章节标题；否则：

- 当首行不是有效章节标题时，程序会使用“第N章 - 预览”作为章节标题，其中“预览”为该章第一段（以空行分隔）的前10个字符，超出部分以“…”显示。
- 建议在文本中保持统一的章节标记格式（如“第1章 标题”或“#标题”）。

## 📁 项目结构

```
Novel_Converter_txt2epub-main/
├── 📄 run.py                 # 启动脚本
├── 📄 example.env            # 配置示例
├── 📄 .env                   # 用户配置文件
├── 📄 requirements.txt       # Python依赖
├── 📄 README.md             # 中文说明文档
├── 📄 README_en.md          # 英文说明文档
├── 📄 USAGE_EXAMPLES.md     # 使用示例文档
├── 📁 assets/               # 资源文件夹
│   └── 🖼️ cover.jpg         # 默认封面图片
├── 📁 novels/               # 小说文件夹
│   └── 📄 novel.txt         # 示例小说文件
└── 📁 src/                  # 源代码
    ├── 📄 __init__.py       # 包初始化
    ├── 📄 main.py          # 主程序入口
    ├── 📄 config.py        # 配置管理
    ├── 📄 chapter_parser.py # 章节解析
    └── 📄 epub_builder.py  # EPUB构建
```

## 🔧 开发说明

项目采用模块化设计，各模块职责明确：

- **`config.py`**: 配置管理和环境变量处理
- **`chapter_parser.py`**: 章节检测和解析逻辑
- **`epub_builder.py`**: EPUB格式构建和保存
- **`main.py`**: 程序流程控制

### 依赖库
- **EbookLib**: EPUB文件生成
- **python-dotenv**: 环境变量管理
- **chardet**: 文本编码检测

## 📚 使用示例

更多详细的使用示例，请参考 [USAGE_EXAMPLES.md](USAGE_EXAMPLES.md) 文档。

## 🐛 常见问题

### Q: 转换后的EPUB文件在哪里？
A: EPUB文件会保存在项目根目录下，文件名为 `{书名}.epub`

### Q: 支持哪些图片格式作为封面？
A: 支持常见的图片格式：JPG, PNG, GIF, BMP等

### Q: 如何处理编码问题？
A: 程序会自动检测文本文件编码，支持UTF-8、GBK、GB2312等常见编码

### Q: 章节检测不准确怎么办？
A: 可以尝试调整 `CHAPTER_DETECTION_METHOD` 配置，或使用特殊字符标记章节

## 📝 更新日志

### v1.1.1
- 修复了章节标题在EPUB中重复显示的问题
- 优化了EPUB生成逻辑，确保章节标题只显示一次

### v1.1.0
- 新增章节标记功能，支持自动为章节标题添加特殊字符
- 支持多种特殊字符标记：#, ##, @, * 等
- 完善了配置选项和文档

### v1.0.0
- 初始版本发布
- 支持多种章节检测方式
- 支持TXT转EPUB转换

## 🤝 贡献

欢迎提交Issue和Pull Request来改进这个项目！

## 📄 许可证

MIT License

## ⭐ 如果这个项目对你有帮助，请给它一个星标！