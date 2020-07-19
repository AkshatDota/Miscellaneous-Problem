def count(i, j):
  c = 0
  while(i>0 and j>0):
    c += 1
    if(i > j):
      i = i - j    ## i = 5, j = 3... i = 2, j = 3... i = 2, j = 1...
    else:           ## i = 1, j = 1, 
      j = j - i
  return c

## 5 x 3



ls = int(input())   # Starting length
le = int(input())   # Ending length
ws = int(input())   # Starting width
we = int(input())   # Ending width
c = 0
for i in range(ls, le+1):   # 5.. 7
  for j in range(ws, we+1):   # 3.. 4
    c += count(i, j)
print(c, end='')







'''
import java.util.*;
class q3
{
  public static int count(int i, int j)
  {
    int c=0;
    while(i>0 && j>0)
    {
        c += 1;
        if(i>j)
            i = i - j;
        else
            j = j - i;
    }
    return c;
  }
  public static void main(String args[])
  {
    Scanner sc = new Scanner(System.in);
    int s = 0;
    int ls = sc.nextInt();
    int le = sc.nextInt();
    int ws = sc.nextInt();
    int we = sc.nextInt();
    for(int i = ls; i<=le; i++)
    {
      for(int j = ws; j <= we; j++)
      {
        s += count(i, j);
      }
    }
    System.out.println(s);
  }
}
'''
