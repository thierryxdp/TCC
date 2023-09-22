#Start your python function here
def filtra_pares(t):
    """tuple->tuple
    a função recebe uma tupla e nos retorna somente os numeros pares presentes nela, na mesma"""
    tupla=tuple(t)
    def inte1():
        if tupla[0]%2==0:
            return 1
    def inte2():
        if tupla[1]%2==0:
            return 1
    def inte3():
        if tupla[2]%2==0:
            return 1
    def inte4():
        if tupla[3]%2==0:
            return 1
    if inte1()==1 and inte2()==1 and inte3()==1 and inte4()==1:
        return str(t)
    elif inte1()==1 and inte2()==1 and inte3()==1:
        return t[0:2]
    elif inte1()==1 and inte2()==1 and inte4()==1:
        return tuple(t[0:1]+t[3])
    elif inte1()==1 and inte3()==1 and inte4()==1:
        return tuple(t[0]+t[2:3])
    elif inte2()==1 and inte3()==1 and inte4()==1:
        return (t[1:3])
    elif inte1()==1 and inte2()==1:
        return t[0:1]
    elif inte1()==1 and inte3()==1:
        return tuple(t[0]+t[2])
    elif inte1()==1 and inte4()==1:
        return tuple(t[0]+t[3])
    elif inte2()==1 and inte3()==1:
        return t[1:2]
    elif inte2()==1 and inte4()==1:
        return '('+tuple(t[1]+t[3])+')'
    elif inte3()==1 and inte4()==1:
        return t[2:3]
    elif inte1()==1:
        return t[0]
    elif inte2()==1:
        return t[1]
    elif inte3()==1:
        return t[2]
    elif inte4()==1:
        return t[3]
    else:
        return '()'