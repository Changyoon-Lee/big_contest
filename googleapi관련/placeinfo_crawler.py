import populartimes
import pickle
from datetime import datetime

api_key = "AIzaSyAZ2_Az5u6JLaVctlXJfYBeHcgBP7Yy2fk"
category = ["cafe", "bank", "bar", "restaurant", "department_store"]
# 하계역 37.635976, 127.068218// 37.640243, 127.063671 에서부터 37.631768, 127.073113
# 을지로입구역 37.566119, 126.982694/ 37.567825, 126.987348 에서부터 37.563877, 126.978664
hagye = [(37.631768, 127.063671), (37.640243, 127.073113)]
eulgi = [(37.563877, 126.978664), (37.567825, 126.987348)]
place = [hagye, eulgi]

now = datetime.now()
dt_str = now.strftime("%m%d%H")
month = dt_str[:2]

data = {}
for i in category:
    data[i] = []
    for pl in place:
        resp = populartimes.get(api_key, [i], pl[0], pl[1], all_places=False)
        data[i].extend(resp)

save_dir = "실시간data/" + month + "/" + dt_str+'.pickle'

with open(save_dir, "wb") as f:
    pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)
    print(month, "폴더에 저장완료")
