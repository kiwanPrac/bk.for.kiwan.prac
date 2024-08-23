student = []

#Add student amount 1 to 30
for i in range(1,31):
    student.append(i)

#remove 28 times, submit student's list
for j in range(28):
    n = int(input())
    student.remove(n)

#print list
for j in range(2):
    print(student[j])
