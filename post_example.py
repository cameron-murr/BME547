import requests

out_data = {
   "name": "Cameron Murr",
   "net_id": "csm57",
   "e-mail": "cameron.murr@duke.edu"
}
r = requests.post("http://vcm-21170.vm.duke.edu:5000/student", json=out_data)
print(r.text)

r2 = requests.get("http://vcm-21170.vm.duke.edu:5000/list")
print(r2.text)
