import requests
import json
import time


def sqlapi(url):
    data = {
        'url': url
    }
    header = {
        'Content-Type': 'application/json'
    }
    task_new_url = "http://127.0.0.1:8775/task/new"
    res = requests.get(task_new_url)
    taskId = res.json()['taskid']
    if 'success' in res.content.decode('utf-8'):
        print('sqlmapapi create success')
        # 进行设置
        task_set_url = 'http://127.0.0.1:8775/option/' + taskId + '/set'
        task_set_res = requests.post(task_set_url, data=json.dumps(data), headers=header)
        if 'success' in task_set_res.content.decode('utf-8'):
            print('setting success')
            # 启动扫描
            task_start_url = 'http://127.0.0.1:8775/scan/' + taskId + '/start'
            task_start_res = requests.post(task_start_url, data=json.dumps(data), headers=header)
            if ('success' in task_start_res.content.decode('utf-8')):
                print('scan start success')
                while 1:
                    task_status_url = 'http://127.0.0.1:8775/scan/' + taskId + '/status'
                    task_status_res = requests.get(task_status_url)
                    if ('running' in task_status_res.content.decode('utf-8')):
                        print('sqlmap are running  ')
                        pass
                    else:
                        task_data_url = 'http://127.0.0.1:8775/scan/' + taskId + '/data'
                        task_data_res = requests.get(task_data_url)
                        f.write(task_data_res.content.decode('utf-8'))
                        break
                time.sleep(3)


if __name__ == '__main__':
    f = open('C:/Users/18876314037/Desktop/res.txt', 'a+')
    for i in open('url.txt', 'r').readlines():
        print(i)
        sqlapi(i)







