# FPSemana03
rom collections import deque

nmb=input("numbers separated: ")

nmbstack=deque(nmb.split())

print(nmbstack)

for i in range(len(nmbstack)):
    element=nmbstack.pop()
    print(int(element)**2)


    from collections import deque

palavras=input("palavras separadas:")

plvstack=deque(palavras.split())

print(plvstack)

for i in range(len(plvstack)):
    elt=plvstack.pop()
    if"o" in elt:
        print(elt)
