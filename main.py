from webserver import keep_alive
import requests

channelID = https://discord.com/channels/946757069858562068/955187861156671559
headers = {
    "authorization":
    "YOUR TOKEN HERE"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
