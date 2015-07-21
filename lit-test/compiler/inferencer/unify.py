# RUN: %python -m artiq.compiler.testbench.inferencer %s >%t
# RUN: OutputCheck %s --file-to-check=%t

a = 1
# CHECK-L: a:int(width='a)

b = a
# CHECK-L: b:int(width='a)

c = True
# CHECK-L: c:bool

d = False
# CHECK-L: d:bool

e = None
# CHECK-L: e:NoneType

f = 1.0
# CHECK-L: f:float

g = []
# CHECK-L: g:list(elt='b)

h = [1]
# CHECK-L: h:list(elt=int(width='c))

i = []
i[0] = 1
# CHECK-L: i:list(elt=int(width='d))

j = []
j += [1.0]
# CHECK-L: j:list(elt=float)

1 if c else 2
# CHECK-L: 1:int(width='f) if c:bool else 2:int(width='f):int(width='f)

True and False
# CHECK-L: True:bool and False:bool:bool

~1
# CHECK-L: ~1:int(width='g):int(width='g)

not True
# CHECK-L: not True:bool:bool

[x for x in [1]]
# CHECK-L: [x:int(width='h) for x:int(width='h) in [1:int(width='h)]:list(elt=int(width='h))]:list(elt=int(width='h))

lambda x, y=1: x
# CHECK-L: lambda x:'i, y:int(width='j)=1:int(width='j): x:'i:(x:'i, ?y:int(width='j))->'i

k = "x"
# CHECK-L: k:str
