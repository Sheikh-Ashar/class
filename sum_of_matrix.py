list_1 = [1,2,3,
          4,5,6,
          7,8,9]
list_2 = [5,6,7,
          8,9,10,
          11,12,13]
sum_list = []
index = 0
for i in list_1:
    sum = i + list_2[index]
    sum_list.append(sum)     
    index += 1

print(sum_list)