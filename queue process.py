from collections import deque

stack1 = deque()
stack2 = deque()
palavras = input()
palavras = palavras.split(" ")

for a in palavras:
    stack1.append(a)
for b in palavras:
    stack2.append(stack1.pop())

print(stack2)

for palavra in palavras:
    if "o" in palavra:
        print(palavra)