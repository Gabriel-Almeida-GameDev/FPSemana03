from collections import deque

intheput = input()
intheput = intheput.split(" ")
stack1 = deque()

for a in intheput:
    stack1.append(int(a))

print(stack1)

for b in range(int(a)):
    valor = stack1.pop()
    valor = valor ** 2
    print(valor)
    
