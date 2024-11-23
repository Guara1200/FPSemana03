from collections import deque

nmb=input("numbers separated: ")

nmbstack=deque(nmb.split())

print(nmbstack)

for i in range(len(nmbstack)):
    element=nmbstack.pop()
    print(int(element)**2)
