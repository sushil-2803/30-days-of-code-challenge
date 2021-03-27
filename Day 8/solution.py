# Enter your code here. Read input from STDIN. Print output to STDOUT
d={}
for _ in range(int(input())):
    p=input().split()
    d[p[0]]=p[1]

while True:
    try:
        name=input()
        if name in d:
            print(f"{name}={d[name]}")
        else:
            print("Not found")
        
    except:
        break
            
            
            