import requests

server = "http://127.0.0.1:5000"

new_patient = {"name": "Chris", "id": 203, "blood_type": "O+"}
r = requests.post(server + "/add_patient", json=new_patient)
print(r.status_code)
print(r.text)

patient_id = "101"
r2 = requests.get(server + "/get_results/" + patient_id)
print(r2.status_code)
print(r2.text)
