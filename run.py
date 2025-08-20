#!/usr/bin/env python3
"""
Novel Converter - TXT to EPUB Converter
启动脚本
"""

import sys
import os

# 添加src目录到Python路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# 导入并运行主程序
from main import main

if __name__ == "__main__":
    main() 