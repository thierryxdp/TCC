#Start your python function here
def filtra_pares(t):
    """tuple->tuple
    a função recebe uma tupla e nos retorna somente os numeros pares presentes nela, na mesma"""
    def inte1():
        if int(t[0])%2==0
    def inte2():
        if int(t[1])%2==0
    def inte3():
        if int(t[2])%2==0
    def inte4():
        if int(t[3])%2==0
    if inte1 and inte2 and inte3 and inte4:
        return t
    elif inte1 and inte2 and inte3:
        return t[0:2]
    elif inte1 and inte2 and inte4:
        return tuple(t[0:1]+t[3])
    elif inte1 and inte3 and inte4:
        return tuple(t[0]+t[2:3])
    elif inte2 and inte3 and inte4:
        return t[1:3]
    elif inte1 and inte2:
        return t[0:1]
    elif inte1 and inte3:
        return tuple(t[0]+t[2])
    elif inte1 and inte4:
        return tuple(t[0]+t[3])
    elif inte2 and inte3:
        return t[1:2]
    elif inte2 and inte4:
        return tuple(t[1]+t[3])
    elif inte3 and inte4:
        return t[2:3]
    elif inte1:
        return t[0]
    elif inte2:
        return t[1]
    elif inte3:
        return t[2]
    elif inte4:
        return t[3]