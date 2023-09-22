#Start your python function here
2
def filtra_pares(t):
3
    """tuple->tuple
4
    a função recebe uma tupla e nos retorna somente os numeros pares presentes nela, na mesma"""
5
    tupla=tuple(t)
6
    def inte1():
7
        if tupla[0]%2==0:
8
            return 1
9
    def inte2():
10
        if tupla[1]%2==0:
11
            return 1
12
    def inte3():
13
        if tupla[2]%2==0:
14
            return 1
15
    def inte4():
16
        if tupla[3]%2==0:
17
            return 1
18
    if inte1()==1 and inte2()==1 and inte3()==1 and inte4()==1:
19
        return t
20
    elif inte1()==1 and inte2()==1 and inte3()==1:
21
        return t[0:2]
22
    elif inte1()==1 and inte2()==1 and inte4()==1:
23
        return tuple(t[0:1]+t[3])
24
    elif inte1()==1 and inte3()==1 and inte4()==1:
25
        return tuple(t[0]+t[2:3])
26
    elif inte2()==1 and inte3()==1 and inte4()==1:
27
        return t[1:3]
28
    elif inte1()==1 and inte2()==1:
29
        return t[0:1]
30
    elif inte1()==1 and inte3()==1:
31
        return tuple(t[0]+t[2])
32
    elif inte1()==1 and inte4()==1:
33
        return tuple(t[0]+t[3])
34
    elif inte2()==1 and inte3()==1:
35
        return t[1:2]
36
    elif inte2()==1 and inte4()==1:
37
        return tuple(t[1]+t[3])
38
    elif inte3()==1 and inte4()==1:
39
        return t[2:3]
40
    elif inte1()==1:
41
        return t[0]
42
    elif inte2()==1:
43
        return t[1]
44
    elif inte3()==1:
45
        return t[2]
46
    elif inte4()==1:
47
        return t[3]