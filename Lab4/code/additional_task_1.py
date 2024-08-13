import xmlplain
import time

start_time = time.time()

with open("schedule_tuesday.yaml", "r", encoding='utf-8') as inf:
    root = xmlplain.obj_from_yaml(inf)

with open("schedule_tuesday.xml", "w", encoding='utf-8') as outf:
    xmlplain.xml_from_obj(root, outf, pretty=True)

print((time.time()-start_time) * 100)