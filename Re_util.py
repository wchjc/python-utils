# @Auther: Ninecats
# @Time: 2021/6/5 14:01
import re


# 邮箱检测
def email(str):
    reg = '^[a-zA-Z0-9_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$'
    if re.match(reg, str):
        return True
    else:
        return False





