def filtra_pares(x):
    '''função que, dados quatro elementos, retorna apenas os elementos pares na ordem de entrada'''
    x0=str(x[0])
    x1=str(x[1])
    x2=str(x[2])
    x3=str(x[3])
    if x[0]%2==0:
        if x[1]%2==0:
            if x[2]%2==0:
                if x[3]%2==0:
                    return x
                else:
                    return x[0:3]
            elif x[3]%2==0:
                 return x[0:2]+x[3]
            else:
                 return x[0:2]
        elif x[2]%2==0:
            if x[3]%2==0:
                return x[0]+[2:]
            else:
                return x[0]+x[2]
        elif x[3]%2==0:
            return x[0]+x[3]
    elif x[1]%2==0:
        if x[2]%2==0:
            if x[3]%2==0:  
                return x[1:]
            else:
                return x[1:3]
        elif x[3]%2==0:
             return x[1:2]+x[3:]
        else:
             return x1
    elif x[2]%2==0:
        if x[3]%2==0:
            return x[2:]
        else:
            return x2
    elif x[3]%2==0:
        return x3
    else:
        return '()'#Start your python function here