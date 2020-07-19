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
    
















            
    
##def gcd(a, b):
##    if b == 0:
##        return a
##    else:
##        return gcd(b, a%b)
##    
##t = int(input())
##for _ in range(t):
##    n = int(input())
##    l = list(map(int, input().split()))
##    i = 0
##    result = 1
##    count = 0
##    while(i <= n-1):
##        temp1 = i
##        count = 0
##        while(l[i] != 0):
##            temp = i
##            i = l[i] - 1
##            l[temp] = 0
##            count += 1
##        i = temp1 + 1
##        if(count != 0):
##            result = result * count // gcd(result, count)
##    print(result)



##    i=0;
##    res=1;
##    c=0;
##    while(i<=n-1)
##    {
##      temp1=i;
##      c=0;
##      while(a[i]!=0)
##      {
##        temp=i;//4
##        i=a[i]-1;//0
##        a[temp]=0;//0
##        c+=1;//3
##      }
##      i=temp1+1;
##      if(c!=0)
##        res=res*c/gcd(res,c);
##    }
##    printf("%lld\n",res);
##  }
##  return 0;
##}
