#8
#234 567 321 345 123 110 767 111
def pairs(n):
    maxi = int(max(str(n))) 
    mini = int(min(str(n)))
    dig = (maxi*11) + (mini * 7)
    if(dig > 99):  
        dig = str(dig)[-2] + str(dig)[-1]
    elif(dig < 10):
        dig = '0' + str(dig)
    return str(dig)
#print(pairs(286))


n = int(input())
l = list(map(int, input().split()))
lst = []
for i in l:
    lst.append(pairs(i))
print(lst)
dic1 = {}
dic2 = {}           # '58'
for i in range(n):
    if(i%2 == 0):
        if lst[i][0] not in dic1:
            dic1[lst[i][0]] = 1
        else:
            dic1[lst[i][0]] += 1
        
    else:
        if lst[i][0] not in dic2:
            dic2[lst[i][0]] = 1
        else:
            dic2[lst[i][0]] += 1


di = {}             # 5:2, # 5:3
for i in dic1:
    if dic1[i] > 1:
        di[i] = dic1[i]
        
for i in dic2:
    if dic2[i] > 1:
        if i not in di:
            di[i] = dic2[i]
        else:
            di[i] = max(di[i], dic2[i])
c = 0
for i in di:
    if di[i] > 2:
        c += 2
    else:
        c += 1
print(c)
