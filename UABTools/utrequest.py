import requests
import common
import json

def downloadJson(url):
    r = requests.get(url)
    return r.json()

def downloadText(url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    return r.text

def post(url, data_):
    r = requests.post(url, json=data_)
    return r.text

def postDingdingText(content):
    print(post(common.DINGDING_POST_TEXT, content))

def postDingdingLink(content):
    print(post(common.DINGDING_POST_LINK, content))

if __name__ == "__main__":
    # r = requests.post(common.DINGDING_POST_LINK, json={
    #     'title':'111',
    #     'text':'test',
    #     'messageUrl':'http://raid-gs.diandian.info:7200/client/package/Android/4elements_2007141658_10029_f_r_0_88_s_rt.apk',
    #     'picUrl': 'https://i.ibb.co/30Sqfmc/image.png',
    # })

    # r = requests.get('https://cli.im/api/qrcode/code?text=http://raid-gs.diandian.info:7200/client/package/Android/4elements_2007141658_10029_f_r_0_88_s_rt.apk')
    # print(r.content)

    # r = requests.get('https://qr.api.cli.im/newqr/down?data=http%3A%2F%2Fraid-gs.diandian.info%3A7200%2Fclient%2Fpackage%2FAndroid%2F4elements_2007141658_10029_f_r_0_88_s_rt.apk&kid=cliim&key=639edf66963d378f51648b8684d191f1&type=png')
    # print(r.content)

    r = requests.get('https://qr.api.cli.im/newqr/create?data=http%3A%2F%2Fraid-gs.diandian.info%3A7200%2Fclient%2Fpackage%2FAndroid%2F4elements_2007141658_10029_f_r_0_88_s_rt.apk&kid=cliim&key=639edf66963d378f51648b8684d191f1')
    print(r.content)
    pass