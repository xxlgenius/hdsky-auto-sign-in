import requests
import json
import captchaparse as cp



result = False
resultmessage = ""
loginurl = "https://hdsky.me/index.php"
imagecodeurl = "https://hdsky.me/image_code_ajax.php"
showupurl = "https://hdsky.me/showup.php"
loginheaders = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
}
postheaders = {
    "content-type" : "application/x-www-form-urlencoded; charset=UTF-8",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/",
    "referer": "https://hdsky.me/index.php",
    "x-requested-with" : "XMLHttpRequest"
}

def PostError(config):
    try:
        with open ("config.json", "r") as f:
            mydata = json.load(f)
    except FileNotFoundError:
        print("配置文件不存在，请检查配置文件是否存在。")
        return
    url = mydata.get("server_host","")
    # 成功post请求
    # 错误post请求
    errorpost = mydata.get("error_post",{})
    errorpost_header = errorpost.get("headers",{})
    errorpost_payload = errorpost.get("payload",{})

def PostSuccess(config):
    try:
        with open ("config.json", "r") as f:
            mydata = json.load(f)
        with open ("cookies.json", "r") as f:
            mycookies = json.load(f)
    except FileNotFoundError:
        print("配置文件不存在，请检查配置文件是否存在。")
        return
    url = mydata.get("server_host","")
    print(url)
    # 成功post请求
    successpost = mydata.get("success_post",{})
    successpost_header = successpost.get("headers",{})
    successpost_payload = successpost.get("payload",{})
    success_response = requests.post(url, headers=successpost_header,cookies=mycookies, data=successpost_payload)
    print(success_response.text)

def getconfig(path):    
    try:
        with open ("config.json", "r") as f:
            myconfig = json.load(f)
    except FileNotFoundError:
        print("配置文件不存在，请检查配置文件是否存在。")
    return myconfig

def getcodefromMD5(hash)->str:
    imgurl = f"https://hdsky.me/image.php?action=regimage&imagehash={hash}"
    imageresponse = requests.get(imgurl)
    if imageresponse.status_code != 200:
        #TODO: 发送错误消息
        exit()
    image_data = imageresponse.content
    imagecode = cp.binary_captchar(image_data)
    return imagecode