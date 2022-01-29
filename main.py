from flask import Flask, jsonify, request
import cv2
import numpy as np
import base64

app = Flask(__name__)

def return_value(is_valid, result_image):
    if not is_valid:
        return jsonify({'result_str': 'False'
        ,'result_image' : "NO"})
    else:
        retval, buffer = cv2.imencode('.jpg', result_image)
        jpg_as_text = base64.b64encode(buffer.tobytes()).decode("utf-8")
        return jsonify({'result_str': 'True'
        , 'result_image':jpg_as_text})

@app.route('/get_image', methods=['POST'])
def get_image():
    if not request.is_json:
        print("Wrong request")
        return return_value(False, None)
    params = request.get_json()
    print(params["USER"])
    encoded_img = params["IMAGE"].encode("utf-8")
    decoded_data = base64.b64decode(encoded_img)
    np_data = np.frombuffer(decoded_data,dtype=np.uint8)
    print(type(np_data))
    img = cv2.imdecode(np_data,cv2.IMREAD_COLOR)
    cv2.imwrite("test.jpg", img)
    return return_value(True, img)


@app.route('/recv_images/<uuid>', methods=['POST'])
def recv_images(uuid):
    print("test", uuid)
    return jsonify({'uuid': uuid})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)