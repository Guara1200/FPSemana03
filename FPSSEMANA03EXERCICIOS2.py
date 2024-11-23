from collections import deque

palavras=input("palavras separadas:")

plvstack=deque(palavras.split())

print(plvstack)

for i in range(len(plvstack)):
    elt=plvstack.pop()
    if"o" in elt:
        print(elt)

