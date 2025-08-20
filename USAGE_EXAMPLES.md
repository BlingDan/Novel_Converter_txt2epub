# 使用示例

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