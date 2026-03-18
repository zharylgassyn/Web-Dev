v = int(input())
t = int(input())
d = v * t
pos = d % 109
if pos > 0 :
    print(pos)
else:
    print(109 + pos)