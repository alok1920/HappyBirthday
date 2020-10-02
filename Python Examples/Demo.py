
try:
    lst = []

    for i in range (0, 100):
        name = input().split()
        lst.append(name)
except:
    lst.pop(0)
    a = lst


def transpose(a, c):  
    c =[[row[i] for row in a] for i in range(len(a[0]))] 
    return c
  
c = [] 


for r in transpose(a, c):
    for c in r:
        print(c, end = " ")
    print()