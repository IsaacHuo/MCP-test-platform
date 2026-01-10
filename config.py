"""
MPMA Configuration File
集中管理 API 配置和模型设置
"""

import os

# =============================================================================
# API 配置
# =============================================================================

# DeepSeek API 配置（默认）
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "your-api-key-here")
DEEPSEEK_BASE_URL = "https://api.deepseek.com"
DEEPSEEK_MODEL = "deepseek-chat"  # DeepSeek-V3.2

# 当前使用的模型配置
DEFAULT_MODEL = "deepseek"

# =============================================================================
# 模型注册表（预留扩展接口）
# =============================================================================

MODELS = {
    "deepseek": {
        "base_url": DEEPSEEK_BASE_URL,
        "api_key": DEEPSEEK_API_KEY,
        "model": DEEPSEEK_MODEL,
    },
    # 后续可添加其他模型：
    # "openai": {
    #     "base_url": "https://api.openai.com",
    #     "api_key": os.environ.get("OPENAI_API_KEY", ""),
    #     "model": "gpt-4o",
    # },
    # "claude": {
    #     "base_url": "https://api.anthropic.com",
    #     "api_key": os.environ.get("ANTHROPIC_API_KEY", ""),
    #     "model": "claude-3-5-sonnet-20241022",
    # },
}


def get_model_config(model_name: str = None) -> dict:
    """获取指定模型的配置
    
    Args:
        model_name: 模型名称，如 "deepseek", "openai" 等
                   如果为 None，则使用默认模型
    
    Returns:
        包含 base_url, api_key, model 的配置字典
    """
    if model_name is None:
        model_name = DEFAULT_MODEL
    
    if model_name not in MODELS:
        raise ValueError(f"Unknown model: {model_name}. Available models: {list(MODELS.keys())}")
    
    return MODELS[model_name]
