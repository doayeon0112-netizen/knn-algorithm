import random as rd
point=[]
for i in range(20):
    x=rd.randint(1,30)
    y=rd.randint(1,10)
    point.append((x,y))
print(point)

rd.shuffle(point)
cuts=sorted(rd.sample(range(1,20),2)) #cuts:1~19
red=point[0:cuts[0]]
green=point[cuts[0]:cuts[1]]
blue=point[cuts[1]:20]

def length(a,b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
    
k=5

while True:
    x=rd.randint(1,30)
    y=rd.randint(1,10)
    if (x,y) in point:
        continue
    else:
        new_point=(x,y)
        break
    
print('새로운 점:',new_point)

for y in range(10,0,-1): #y:10~1
    for x in range(1,31): #x:1~30
        if (x,y) in red:
            print(' r ',end='')
        elif (x,y) in green:
            print(' g ',end='')
        elif (x,y) in blue:
            print(' b ',end='')
        elif (x,y) == new_point:
            print(' x ',end='')
        else:
            print(' - ',end='')
    print()

length_list=[]
for i in red:
    length_list.append(('red',length(i,new_point)))
for i in green:
    length_list.append(('green',length(i,new_point)))
for i in blue:
    length_list.append(('blue',length(i,new_point))) #length_list=[('red',3.5),('blue',5)...]

length_list.sort(key=lambda x:x[1])
res_list=length_list[:k]

count={'red':0,'green':0,'blue':0}
for i in res_list:
    if i[0]=='red':
        count['red']+=1
    elif i[0]=='green':
        count['green']+=1
    elif i[0]=='blue':
        count['blue']+=1 #count={'red':1,'green':3,'blue':1}

res='red'
big=count['red']
if count['green']>big:
    res='green'
    big=count['green']
if count['blue']>big:
    res='blue'

print('새로운 점은',res,'군집에 속합니다')
