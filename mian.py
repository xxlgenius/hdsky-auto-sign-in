import requests
import json
import captchaparse as cp
import config
import hashlib

myconfig = config.getconfig("config.json")


def main():
    mycookies = myconfig.get("cookies",{})
    response = requests.get(config.loginurl, headers=config.loginheaders, cookies=mycookies)
    if response.history:
        config.resultmessage = f"登陆失败发生了重定向，最终的URL是: {response.url}"
    else:# 尝试三次读取验证码
        for i in range(0,3): 
            coderesponse = requests.post(config.imagecodeurl, headers=config.postheaders, cookies=mycookies, data="action=new")
            if coderesponse.status_code != 200:
                config.resultmessage = f"获取验证码的post方法发送失败:{coderesponse_json}"
                continue
            coderesponse_json = coderesponse.json()
            coderesponse_hash = coderesponse_json.get("code","")
            coderesponse_state = coderesponse_json.get("success",False)
            if coderesponse_state == False:
                config.resultmessage = f"获取验证码哈希值失败:{coderesponse_json}"
                continue
            code = config.getcodefromMD5(coderesponse_hash).upper()
            print(f"哈希值是:{coderesponse_hash}")
            print(f"验证码是:{code}")
            sign_in_response = requests.post(config.showupurl, headers=config.postheaders, cookies=mycookies, data=f"action=showup&imagehash={coderesponse_hash}&imagestring={code}")
            if sign_in_response.status_code != 200:
                config.resultmessage = f"签到post请求失败:{sign_in_response.text}"
                continue
            coderesponse_json = sign_in_response.json()
            if coderesponse_json.get("success",False) == True:
                config.resultmessage = "签到成功"
                config.result = True
                break
            else:
                res = coderesponse_json.get('message','')
                if res == 'date_unmatch':
                    config.resultmessage = "日期不对，今日已经签到"
                    break
                config.resultmessage = f"签到失败:{res}"
                continue
    if config.result == True:
        print("成功签到")
    else:
        print(f"签到失败,{config.resultmessage}")  
        
if __name__ == "__main__":
    main()