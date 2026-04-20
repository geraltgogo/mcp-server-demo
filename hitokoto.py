"""
FastMCP quickstart example.

Run from the repository root:
    uv run /Users/geralt/VsCode_project/mcp-server-demo/hitokoto.py
"""

import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("hitokoto", log_level="ERROR", json_response=True)

url = "https://v1.hitokoto.cn/"


@mcp.tool()
def fetch_hitokoto(c: str) -> dict:
    """
    访问接口，获取每日一言的功能
    参数:
        c: 每日一言的类型，a=动画，b=漫画，c=游戏，d=文学，e=原创，f=来自网络，g=其他，h=影视，i=诗词，j=网易云，k=哲学，l=抖机灵
    Returns:
        dict: 包含句子信息的字典，包括 hitokoto(句子)、from(出处)、from_who(作者)等字段
    """
    try:
        params = {'c': c}
        response = httpx.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except httpx.RequestError as e:
        raise Exception(f"请求失败: {e}")
    except ValueError as e:
        raise Exception(f"解析响应失败: {e}")

if __name__ == '__main__':
    mcp.run(transport='stdio')
