import requests

r = requests.get(
    "http://vcm-7631.vm.duke.edu:5002/get_patients/csm57")

answer = r.json()

id1 = answer["Donor"]
id2 = answer["Recipient"]

b_donor = requests.get(
    "http://vcm-7631.vm.duke.edu:5002/get_blood_type/" + id1)
b_recipient = requests.get(
    "http://vcm-7631.vm.duke.edu:5002/get_blood_type/" + id2)

print(b_donor.text, b_recipient.text)

out_data = {"Name": "csm57", "Match": "No"}

r2 = requests.post(
    "http://vcm-7631.vm.duke.edu:5002/match_check", json=out_data)

print(r2.text)
