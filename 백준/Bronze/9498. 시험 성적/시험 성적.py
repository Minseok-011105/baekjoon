Grade = int(input())

if Grade >= 90:
    print('A')
elif (Grade < 90 and Grade >= 80):
    print('B')
elif (Grade < 80 and Grade >= 70):
    print('C')
elif (Grade < 70 and Grade >= 60):
    print('D')
else:
    print('F')
    