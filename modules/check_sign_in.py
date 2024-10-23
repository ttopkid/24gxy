import requests
from modules.load_config import dprint
from datetime import datetime, timedelta


# 查用户是否已经打卡
def check_sign(check_sign_token, sign_type):
    check_sign_url = "https://api.moguding.net:9000/attendence/clock/v2/listSynchro"
    # 获取整个月的打卡信息
    # search_start_time, search_end_time = get_current_month()

    # 获取当天的打卡信息
    search_start_time, search_end_time = get_current_day()
    data = {
        "startTime": search_start_time,
        "endTime": search_end_time,
    }
    headers = {"Authorization": f"{check_sign_token}"}
    response = requests.post(check_sign_url, json=data, headers=headers)
    response_data = response.json()

    # ❗开发环境输出, 打印打卡记录的响应内容
    # dprint(response_data)

    # 检查是否有过打卡记录
    for record in response_data["data"]:
        if record["type"] == sign_type:
            # 打过卡
            return True
    # 没打过卡
    return False


# 获取当前月份起始时间
# 这里的具体时间无所谓，返回的内容是全天的签到记录, 写时间是因为标准的时间格式要求
# def get_current_month():
#     now = datetime.now()
#     start_of_month = datetime(now.year, now.month, 1)
#     if now.month == 12:
#         next_month_start = datetime(now.year + 1, 1, 1)
#     else:
#         next_month_start = datetime(now.year, now.month + 1, 1)
#     end_of_month = next_month_start - timedelta(days=1)
#     month_start_time = start_of_month.strftime("%Y-%m-%d %H:%M:%S")
#     month_end_time = end_of_month.strftime("%Y-%m-%d 00:00:00")
#     return month_start_time, month_end_time


# 获取当天起始时间
def get_current_day():
    now = datetime.now()
    start_of_day = datetime(now.year, now.month, now.day)
    end_of_day = start_of_day + timedelta(days=1, seconds=-1)
    day_start_time = start_of_day.strftime("%Y-%m-%d 00:00:00")
    day_end_time = end_of_day.strftime("%Y-%m-%d 23:59:59")
    return day_start_time, day_end_time


# 开发环境测试环境解除注释
# dprint("\n❗注意：以下输出是check_sign模块的开发环境信息，👇")
# day_start_time, day_end_time = get_current_day()
# dprint("打卡信息查询日期范围:\n", day_start_time, "→", day_end_time)
# check_sign(
#     check_sign_token="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
#     sign_type="START",
# )
