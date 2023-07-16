import base64
import json
import requests

base64_string = base64.b64encode("\n\vDVa4tfzpZ90".encode("utf-8")).decode("utf-8")

headers = {
    "Content-Type": "application/json",
}

body = json.dumps(
    {
        "context": {"client": {"clientName": "WEB", "clientVersion": "2.9999099"}},
        "params": base64_string,
    }
)

response = requests.post(
    "https://www.youtube.com/youtubei/v1/get_transcript?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8",
    headers=headers,
    data=body,
)

print(response.text)
