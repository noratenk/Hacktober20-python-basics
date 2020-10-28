number = '1s2'
task1_list = [123, 'abc15', True, [4, 9, 12, 'a'],
              {1: 'Egy', 2: 'ketto', 3: 'harom', 4: 'ot'}]
number = number.translate({ord('s'): None})
number = int(number)
task1_list.append(number)
print ("A szám 10-szerese:", task1_list[0]*10)
print ("A szám négyzete:", task1_list[0]**2)
b1 = task1_list[1][0:3]
b2 = task1_list[1][3:]
task1_list.insert(0, b2)
task1_list.insert(0, b1)
hossz = 0
for i in range(len(task1_list[5])):
    hossz += 1
if hossz > 5:
    print('Igaz')
else:
    print('Hamis')
osszeg = 0
for j in range(len(task1_list[5])-1):
    osszeg +=task1_list[5][j]
del task1_list[5][-1]
task1_list[5].append(osszeg)
task1_list[6][4]='negy'
task1_list[6][5]= 'OT'
task1_list[6] = {key: list(map(str.upper, task1_list[6][key])) for key in task1_list[6]} 
print(task1_list)