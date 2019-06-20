a=input()
b=[]
for i in a:
    if i not in b:
        b.append(i)
    else:
        break
print(len(b))
