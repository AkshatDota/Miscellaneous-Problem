n = int(input())
bride = list(input())  # ['r','m','r','m']
groom = list(input())  # ['m','m']
for i in bride:
    if(i in groom):
      groom.remove(i)
    else:
      break
print(len(groom))
