'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

T = int(input("test cases:"))

for i in range(T):
    F,K,N = map(int,input("F,K,N: ").split())
    no_time_list=[]
    full_time=set(range(0,F+1))
    
    for j in range(N):
        Si,Ei = map(int,input("interval: ").split())
        l = [x for x in range(Si,Ei)]
        no_time_list.extend(l)
        
    no_time=set(no_time_list)
    print(full_time)
    print(no_time)
    free_time=full_time.difference(no_time)
    print(free_time)
    
    free_minutes = len(free_time)
    if free_minutes >= K:
        print("YES")
    else:
        print("NO")
    