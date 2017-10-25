import random

a = random.randrange(0,2)
if a==0:
    a = 'O'
else:
    a = 'X'

b = random.randrange(0,2)
if b==0:
    b = 'O'
else:
    b = 'X'

c = random.randrange(0,2)
if c==0:
    c = 'O'
else:
    c = 'X'

d = random.randrange(0,2)
if d==0:
    d = 'O'
else:
    d = 'X'

e = random.randrange(0,2)
if e==0:
    e = 'O'
else:
    e = 'X'

f = random.randrange(0,2)
if f==0:
    f = 'O'
else:
    f = 'X'

g = random.randrange(0,2)
if g==0:
    g = 'O'
else:
    g = 'X'

h = random.randrange(0,2)
if h==0:
    h = 'O'
else:
    h = 'X'

i = random.randrange(0,2)
if i==0:
    i = 'O'
else:
    i = 'X'


Win_Combination = (
    (a, b, c), (d, e, f), (g, h, i),   #Win Horizontal
     (a, d, g), (b, e, h), (c, f, i),  #Win vertical
     (a, e, i), (c, e, g))             #Win diagonal


print(a, b, c)
print(d, e, f)
print(g, h, i)
print()

if a == b and b ==  c:
    print ('Win')
    exit
elif d == e and e == f:
    print ('Win')
    exit
elif g == h and h == i:
    print ('Win')
    exit
elif a == d and d == g:
    print ('Win')
    exit
elif b == e and e == h:
    print ('Win')
    exit
elif c == f and f == i:
    print ('Win')
    exit
elif a == e and e == i:
    print ('Win')
    exit
elif c == e and e == g:
    print ('Win')
    exit
