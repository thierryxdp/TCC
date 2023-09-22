def filtra_pares(numero1,numero2,numero3,numero4):
    a=int(numero1)%2
    b=int(numero2)%2
    c=int(numero3)%2
    d=int(numero4)%2 
    if a==0 and a==b and b==c and c==d:
        return [numero1,numero2,numero3,numero4]
    elif not a==0 and not b==0 and not c==0 and not d==0:
        return ' sem valor par'
    elif a==0 and b==0 and c==0 and not d==0:
        return [numero1,numero2,numero3]
    elif a==0 and b==0 and not c==0 and d==0:
        return [numero1,numero2,numero4]
    elif a==0 and not b==0 and c==0 and d==0:
        return [numero1,numero3,numero4]
    elif not a==0 and b==0 and c==0 and d==0:
        return [numero2,numero3,numero4]
    elif a==0 and not b==0 and not c==0 and not d==0:
        return [numero1]
    elif a==0 and b==0 and not c==0 and not d==0:
        return [numero1,numero2]
    elif a==0 and not b==0 and c==0 and not d==0:
        return [numero1,numero4]
    elif a==0 and not b==0 and not c==0 and d==0:
        return [numero1,numero4]  
    elif not a==0 and b==0 and not c==0 and not d==0:
        return [numero2]
    elif not a==0 and b==0 and c==0 and not d==0:
        return [numero2,numero3]
    elif not a==0 and b==0 and not c==0 and d==0:
        return [numero2,numero4]
    elif not a==0 and not b==0 and c==0 and not d==0:
        return [numero3]
    elif not a==0 and not b==0 and c==0 and d==0:
        return [numero3,numero4]
    elif not a==0 and not b==0 and not c==0 and d==0:
        return [numero4]
    #Start your python function here