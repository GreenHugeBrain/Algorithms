def team():
    problemint = int(input())
    result = 0
    for n in range(problemint):
        teamsolution = input().split()
        arr = []
        for i in teamsolution:
            int(i)
            arr.append(int(i))
            
        if arr[0] + arr[1] + arr[2] > 1:
            result += 1
        
    print(result)
                                                                                                                            

team()                                  