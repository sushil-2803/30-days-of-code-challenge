# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range (int(input())):
    s=input()
    se,so='',''
    se=s[0]
    for j in range(1,len(s)):
        if j%2==0:
            se=se+s[j]
        else:
            so=so+s[j]
    print(se,so)