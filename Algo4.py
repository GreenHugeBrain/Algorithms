def timur():
    case = int(input())
    correct_name = 'Timur'
    arr = []
    for i in range(case):
        lenght = int(input())
        name = input()
    for letter in name:
        if letter in correct_name:
            arr.append('YES')
        else:
            arr.append('NO')    
                        
    for r in arr:
        print(r)
timur()