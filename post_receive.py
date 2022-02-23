import requests

out_data = {"user": "PranavSharma", "message": "heyo bb"}

r = requests.post(
    "http://vcm-21170.vm.duke.edu:5001/add_message", json=out_data)
print(r.text)

r2 = requests.get(
    "http://vcm-21170.vm.duke.edu:5001/get_messages/CameronMurr")
print(r2.status_code)

if r2.status_code == 200:
    print(r2.text)
