list = input().split()
list_of_none_zeros = []
list_of_zeros = []
for i in range(len(list)):
    if list[i] != '0':
        list_of_none_zeros.append(list[i])
    else:
        list_of_zeros.append(list[i])



print(list_of_none_zeros + list_of_zeros)
    