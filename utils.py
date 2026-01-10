"""
MPMA Utility Functions
通用工具函数
"""

# 注意：API 调用相关功能已迁移到 llm_client.py
# 此文件保留用于其他工具函数

from llm_client import query as openai_query  # 向后兼容的别名


def format_description(description: str, prefix: str = "") -> str:
    """格式化工具描述
    
    Args:
        description: 原始描述
        prefix: 可选前缀
    
    Returns:
        格式化后的描述
    """
    if prefix:
        return f"{prefix} {description}"
    return description