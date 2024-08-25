#create empty list
list = []

for i in range(10):
    A = int(input())
    temp = A % 42
    # A % 42 amount will add to list
    list.append(temp)
# Using set delete same value
set_list = set(list)
print(len(set_list))