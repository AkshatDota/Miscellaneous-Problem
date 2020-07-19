def lcm(a, b):
    small = min(a, b)
    large = max(a, b)
    rem = large % small
    while(rem != 0): 
        large = small
        small = rem
        rem = large % small
    gcd = small 
    lcm = (a*b)//gcd
    return lcm


t = int(input())
for _ in range(t):
    n = int(input())
    ar = list(map(int, input().split()))
    ar.insert(0, 0)
    dance = set()
    for i in range(1, n+1):
        if(ar[i] == 0):
            continue
        current = i
        block = i
        count = 0
        while(1):
            current = ar[current]
            ar[block] = 0
            block = current
            count += 1
            if(current == i):
                break
        dance.add(count)
        
    dance = list(dance)                   ##   ar = [ 4, 5, 2, 1]  [20,2],.... [20,1]
    ans = lcm(dance[0], dance[1])
    for i in range(2, len(dance)):
        ans = lcm(ans, dance[i])
        
    print(ans)
    
