import requests
import time

token = "ODQ3NDI0OTgyMjQ2MzU5MDYx.YK94Ig.UEAy3paCjWK8k2H8qhZ1At-hljo"  # token
channelId = "849908942687043604"  # channel id

while True:
    requests.post("https://discord.com/api/v8/channels/" +
                  channelId + "/messages", json={"content": "!d bump"},
                  headers={"Authorization": token})
    time.sleep(7210)