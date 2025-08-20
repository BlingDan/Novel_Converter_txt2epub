import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

class Config:
    """配置类，管理所有配置参数"""
    
    @staticmethod
    def get_txt_file():
        """获取TXT文件路径"""
        return os.getenv('TXT_FILE')
    
    @staticmethod
    def get_cover_image():
        """获取封面图片路径"""
        return os.getenv('COVER_IMAGE')
    
    @staticmethod
    def get_title():
        """获取书籍标题"""
        return os.getenv('TITLE')
    
    @staticmethod
    def get_author():
        """获取作者信息"""
        return os.getenv('AUTHOR')
    
    @staticmethod
    def get_chapter_detection_method():
        """获取章节检测方法"""
        method = os.getenv('CHAPTER_DETECTION_METHOD', 'auto')
        return method.lower()
    
    @staticmethod
    def enable_double_empty_line_detection():
        """是否启用双空行分章检测"""
        return os.getenv('ENABLE_DOUBLE_EMPTY_LINE', 'true').lower() == 'true'
    
    @staticmethod
    def enable_chapter_marker():
        """是否启用章节标记功能（在双空行分章时添加特殊字符）"""
        return os.getenv('ENABLE_CHAPTER_MARKER', 'false').lower() == 'true'
    
    @staticmethod
    def get_chapter_marker():
        """获取章节标记字符"""
        return os.getenv('CHAPTER_MARKER', '#')
    
    @staticmethod
    def validate_config():
        """验证配置是否完整"""
        required_fields = ['TXT_FILE', 'TITLE', 'AUTHOR']
        missing_fields = []
        
        for field in required_fields:
            if not os.getenv(field):
                missing_fields.append(field)
        
        if missing_fields:
            print(f"缺少必要的环境变量: {', '.join(missing_fields)}")
            return False
        
        return True 