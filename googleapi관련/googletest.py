import populartimes

# a = populartimes.get ("AIzaSyAZ2_Az5u6JLaVctlXJfYBeHcgBP7Yy2fk",['cafe'] (48.132986, 11.566126), (48.142199, 11.580047))
# print(a)

a = populartimes.get_id("your-api-key", "ChIJSYuuSx9awokRyrrOFTGg0GY")

min = (37.427661, 126.766876)
max = (37.698634, 127.181338)
k = 0.063
s_lat, s_lon = min[0], max[0]
while :
    data = populartimes.get("AIzaSyC0CYfCgDfSlM4BN_tPCbtdxioaRewH1IM", ['cafe'] ,(s_lat, s_lon), (s_lat+k, s_lon+k),all_places = False)




def __init__(self):
    self.csvwriter = csv.writer(open('naver.csv','w', encoding='utf-8'))
    self.csvwriter.writerow(['media','time','body'])
def process_item(self, item, spider):
    row=[]
    row.append(item['media'])
    row.append(item['time'])
    row.append(item['body'])
    self.csvwriter.writerow(row)
    return item




