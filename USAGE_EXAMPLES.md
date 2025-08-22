# 使用示例

## 路径配置示例

### 路径配置说明

在配置 `.env` 文件时，文件路径的配置非常重要。推荐使用绝对路径以避免路径解析错误。

### 示例1：Windows 系统路径配置

**配置文件 `.env`**：
```env
# 使用绝对路径（推荐）
TXT_FILE=C:/Users/YourName/Desktop/Novel_Converter_txt2epub-main/novels/novel.txt
COVER_IMAGE=C:/Users/YourName/Desktop/Novel_Converter_txt2epub-main/assets/cover.jpg
TITLE=我的小说
AUTHOR=作者名
```

### 示例2：macOS/Linux 系统路径配置

**配置文件 `.env`**：
```env
# 使用绝对路径（推荐）
TXT_FILE=/home/username/Desktop/Novel_Converter_txt2epub-main/novels/novel.txt
COVER_IMAGE=/home/username/Desktop/Novel_Converter_txt2epub-main/assets/cover.jpg
TITLE=我的小说
AUTHOR=作者名
```

### 示例3：相对路径配置（备选方案）

**配置文件 `.env`**：
```env
# 使用相对路径（需要确保文件在正确位置）
TXT_FILE=./novels/novel.txt
COVER_IMAGE=./assets/cover.jpg
TITLE=我的小说
AUTHOR=作者名
```

## 章节标记功能使用示例

### 示例1：基本使用

**原始TXT文件内容**：
```
第一章 故事开始

这是第一章的内容。
这里有一些段落。



第二章 情节发展

这是第二章的内容。
情节开始发展。



第三章 高潮部分

这是第三章的内容。
故事达到高潮。
```

**配置文件 `.env`**：
```env
TXT_FILE=./novels/novel.txt
COVER_IMAGE=./assets/cover.jpg
TITLE=我的小说
AUTHOR=作者名
CHAPTER_DETECTION_METHOD=auto
ENABLE_DOUBLE_EMPTY_LINE=true
ENABLE_CHAPTER_MARKER=true
CHAPTER_MARKER=#
```

**生成的EPUB中的章节标题**：
```
#第一章 故事开始
#第二章 情节发展
#第三章 高潮部分
```

**注意**：章节标题在EPUB中只会显示一次，不会出现重复显示的问题。

### 示例2：使用不同标记字符

**配置文件 `.env`**：
```env
ENABLE_CHAPTER_MARKER=true
CHAPTER_MARKER=##
```

**生成的EPUB中的章节标题**：
```
##第一章 故事开始
##第二章 情节发展
##第三章 高潮部分
```

### 示例3：使用@标记

**配置文件 `.env`**：
```env
ENABLE_CHAPTER_MARKER=true
CHAPTER_MARKER=@
```

**生成的EPUB中的章节标题**：
```
@第一章 故事开始
@第二章 情节发展
@第三章 高潮部分
```

### 示例4：不启用章节标记

**配置文件 `.env`**：
```env
ENABLE_CHAPTER_MARKER=false
```

**生成的EPUB中的章节标题**：
```
第一章 故事开始
第二章 情节发展
第三章 高潮部分
```

## 支持的章节格式示例

### 特殊字符标记
```
#第一章 故事开始
##第二章 情节发展
@第三章 高潮部分
```

### 数字格式
```
第1章 标题
第 1 章 标题
第1000章 标题
Chapter 1 标题
Section 1 标题
```

### 中文数字格式
```
第一章 标题
第一百章 标题
第一千章 标题
第一节 标题
第一部 标题
```

### 其他格式
```
1. 标题
1、标题
一、标题
一百、标题
```

## 微信读书使用示例

### 示例1：为微信读书优化的配置

**配置文件 `.env`**：
```env
TXT_FILE=./novels/novel.txt
COVER_IMAGE=./assets/cover.jpg
TITLE=我的小说
AUTHOR=作者名
CHAPTER_DETECTION_METHOD=auto
ENABLE_DOUBLE_EMPTY_LINE=true
ENABLE_CHAPTER_MARKER=true
CHAPTER_MARKER=#
```

**说明**：
- 启用章节标记功能，使章节标题在微信读书中更加醒目
- 使用 `#` 作为章节标记，在微信读书中显示效果最佳
- 自动检测章节，确保微信读书的目录功能正常工作

### 示例2：微信读书导入流程

1. **生成EPUB文件**
   ```bash
   python run.py
   ```

2. **导入到微信读书**
   - 打开微信读书APP
   - 点击"书架" → "导入"
   - 选择生成的 `我的小说.epub` 文件
   - 等待导入完成

3. **验证导入结果**
   - 检查书籍是否出现在书架中
   - 确认封面是否正确显示
   - 验证章节目录是否完整
   - 测试章节跳转功能

### 示例3：微信读书阅读体验优化

**推荐的章节格式**：
```
#第一章 故事开始
这是第一章的内容...

#第二章 情节发展
这是第二章的内容...

#第三章 高潮部分
这是第三章的内容...
```

**优化效果**：
- 章节标题在微信读书中显示为 `#第一章 故事开始`
- 支持微信读书的章节跳转功能
- 在目录中清晰显示所有章节
- 提供良好的阅读体验

### 示例4：处理微信读书特殊需求

**对于没有明确章节标记的文本**：
```env
CHAPTER_DETECTION_METHOD=double_empty_line_only
ENABLE_CHAPTER_MARKER=true
CHAPTER_MARKER=#
```

**原始文本**：
```
故事开始

这是第一章的内容...



情节发展

这是第二章的内容...
```

**生成的EPUB在微信读书中的效果**：
- 自动识别章节分隔
- 添加章节标记：`#故事开始`、`#情节发展`
- 在微信读书中正确显示章节结构

## 配置选项说明

### 章节检测方法
- `auto`: 自动模式，优先使用模式匹配，双空行作为兜底
- `pattern_only`: 仅使用模式匹配
- `double_empty_line_only`: 仅使用双空行检测

### 章节标记功能
- `ENABLE_CHAPTER_MARKER=true`: 启用章节标记功能
- `ENABLE_CHAPTER_MARKER=false`: 禁用章节标记功能（默认）

### 标记字符
- `CHAPTER_MARKER=#`: 使用#作为标记
- `CHAPTER_MARKER=##`: 使用##作为标记
- `CHAPTER_MARKER=@`: 使用@作为标记
- `CHAPTER_MARKER=*`: 使用*作为标记

## 运行步骤

1. **准备文件**：
   - 将TXT文件放在 `novels/` 目录下
   - 将封面图片放在 `assets/` 目录下

2. **配置环境**：
   - 复制 `example.env` 为 `.env`
   - 修改配置参数

3. **运行转换**：
   ```bash
   python run.py
   ```

4. **查看结果**：
   - 生成的EPUB文件会保存在项目根目录
   - 文件名格式：`{TITLE}.epub`

## 技术说明

### 章节标题处理
- 章节标题在EPUB中只显示一次，避免重复显示
- 标题使用 `<h1>` 标签，内容使用 `<p>` 标签
- 自动分离标题和内容，确保格式正确

### 输出格式
- 章节标题：`<h1>#第一章 故事开始</h1>`
- 章节内容：`<p>这是第一章的内容...</p>`
- 不会出现标题重复显示的问题 