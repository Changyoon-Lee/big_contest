import populartimes
import pickle
from datetime import datetime
import os

api_key = ""
category = ["cafe", "bank", "bar", "restaurant", "department_store"]
# 하계역 37.635976, 127.068218// 37.640243, 127.063671 에서부터 37.631768, 127.073113
# 을지로입구역 37.565969, 126.982572// 37.566119, 126.982694/ 37.567825, 126.987348 에서부터 37.563877, 126.978664
hagye = [(37.640052, 127.066330), (37.634432, 127.071865)]
eulgi = [(37.565969, 126.982572), (37.567768, 126.985686)]
place = [hagye, eulgi]

now = datetime.now()
dt_str = now.strftime("%m%d%H")
month = dt_str[:2]

data = {}
for i in category:
    data[i] = []
    for pl in place:
        try:
            resp = populartimes.get(api_key, [i], pl[0], pl[1], all_places=False)
            data[i].extend(resp)
        except:print('-----error-----','\n카테고리:{}\n좌표1:{}\n좌표2:{}'.format(i,pl[0], pl[1]))

save_dir = os.path.join(os.getcwd(),'실시간data',  month, dt_str+'.pickle')
print(os.path.exists(save_dir))
####dir 없으면 생성해주는 함수 만들면 좋겠다###

with open(save_dir, "wb") as f:
    pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)
    print(month, "폴더에 저장완료")
