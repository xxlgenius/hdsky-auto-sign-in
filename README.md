# hdsky-auto-sign-in
一个HSDsky自动签到脚本
该脚本通过使用opencv来识别验证码，准确率几乎可以说100%

HDsky是通过一个MD5来生成验证码图片的，所以如果觉得opencv太笨重，可以找暴力破解MD5的网站API,直接将MD5转成验证码，但正确率不明
## 使用
1. 在根目录创建一个`config.json`文件，写入HDsky的cookie就可以了
2. （可选）[还没实现] 在`config.json`写入HTTP POST的请求可以在发生错误或成功的时候发送HTTP消息
### config.json
```json
{
    "cookies": {
    "c_secure_login": "",
    "c_secure_pass": "",
    "c_secure_ssl": "",
    "c_secure_tracker_ssl": "",
    "c_secure_uid": ""
    },
    "server_host": "POST接收服务器",
    "success_post": {
        "headers": {},
        "payload": {}
    },
    "error_post": {
        "headers":{},
        "payload":{}
    }
}
```