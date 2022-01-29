import requests
import cv2
import base64
import json
import numpy as np
test_image = cv2.imread("test_image.jpeg", cv2.IMREAD_COLOR)
retval, buffer = cv2.imencode('.jpg', test_image)
print(type(buffer))
jpg_as_text = base64.b64encode(buffer.tobytes()).decode("utf-8")

API_HOST = 'http://192.168.0.8:8080/'
headers = {'request': 'ID_ROKEN'}

def req(path, query, method, json={}):
    url = API_HOST + path
    print('HTTP Method: %s' % method)
    print('Request URL: %s' % url)
    print('Headers: %s' % headers)
    print('QueryString: %s' % query)

    if method == 'GET':
        return requests.get(url, headers=headers)
    else:
        return requests.post(url, headers=headers, json=json)

data = {
    "USER":"TEST_USER",
    "IMAGE":jpg_as_text
    }
data_json = json.dumps(data)
resp = req('/get_image', '', 'POST', json=data)
print("response status:\n%d" % resp.status_code)
print("response headers:\n%s" % resp.headers)
#print("response body:\n%s" % resp.text)
result_text = json.loads(resp.text)
print(result_text["result_str"])

encoded_img = result_text["result_image"].encode("utf-8")
decoded_data = base64.b64decode(encoded_img)
np_data = np.frombuffer(decoded_data,dtype=np.uint8)
img = cv2.imdecode(np_data,cv2.IMREAD_COLOR)
cv2.imshow("img", img)
cv2.waitKey(0)