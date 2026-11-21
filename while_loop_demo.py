import random
a = 0
list = []
while a <= 10:
    
    a += 1
    
    list.append(a)
    print(list)
    rand_num = (random.shuffle(list[0:]))
    print(rand_num)
