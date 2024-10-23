import requests
from modules.load_config import dprint


# 推送消息到PushPlus
def push_to_pushplus(users, title, content, token):
    url = (
        "http://www.pushplus.plus/send?token="
        + token
        + "&title="
        + title
        + "&content="
        + content
        + "&template=html"
    )
    resp = requests.post(url)
    result = resp.json()

    if result["code"] == 200:
        for user in users:
            dprint(f'[{user["remark"]}/{user["phone"]}]', end="")
            print(f"√ 用户消息推送成功！", end="")
            dprint(f"响应内容: {resp.text}")
    else:
        for user in users:
            dprint(f'[{user["remark"]}/{user["phone"]}]', end="")
            print(f"X 推送消息提醒失败！", end="")
            dprint(f"响应内容: {resp.text}")
