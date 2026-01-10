"""
MPMA LLM Client
统一的 LLM API 调用模块
"""

import json
import requests
from typing import Optional

from config import get_model_config


def query(
    prompt: str,
    query_text: str,
    model_name: str = None,
    max_retries: int = 100,
) -> str:
    """统一的 LLM 查询接口
    
    Args:
        prompt: 系统提示词
        query_text: 用户查询内容
        model_name: 模型名称（可选，默认使用配置中的默认模型）
        max_retries: 最大重试次数
    
    Returns:
        LLM 返回的响应文本
    """
    config = get_model_config(model_name)
    
    payload = json.dumps({
        "model": config["model"],
        "messages": [
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": query_text
            }
        ]
    })
    
    url = f"{config['base_url']}/v1/chat/completions"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {config['api_key']}",
        "Content-Type": "application/json"
    }
    
    attempts = 0
    while attempts < max_retries:
        try:
            response = requests.post(url, headers=headers, data=payload, timeout=60)
            data = response.json()
            result = data["choices"][0]["message"]["content"]
            print(f"Successfully queried {config['model']}")
            return result
        except Exception as e:
            attempts += 1
            print(f"Query attempt {attempts} failed: {e}")
            if attempts >= max_retries:
                raise RuntimeError(f"Failed to query LLM after {max_retries} attempts")
    
    return ""


def query_batch(
    prompts: list[tuple[str, str]],
    model_name: str = None,
) -> list[str]:
    """批量查询接口
    
    Args:
        prompts: (system_prompt, user_query) 元组列表
        model_name: 模型名称
    
    Returns:
        响应文本列表
    """
    results = []
    for system_prompt, user_query in prompts:
        result = query(system_prompt, user_query, model_name)
        results.append(result)
    return results
