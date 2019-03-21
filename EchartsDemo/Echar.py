from pyecharts import Bar

f = open("E:\\IDEA_workspace\\BigData_Long\\pydemo\\file\\data.txt",encoding='utf-8')
lines = f.readlines()
list_id = []
list_name = []
for l in lines:
    arr = l.split(",")
    if arr.__len__()>1:
        id = arr[0].split(": ")
        id1 = id[1]
        name = arr[1].split(": ")
        name1 = name[1][1:-1]
        list_id.append(id1)
        list_name.append(name1)
f.close()
bar =Bar("我的第一个图表", "这里是副标题")
print(list_id)
print(list_name)
bar.add("城市统计", list_name, list_id)
bar.show_config()
bar.render("E:\\IDEA_workspace\\BigData_Long\\EchartsDemo\\html\\echar.html")