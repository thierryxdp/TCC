def filtra_pares(tup):
    '''fução que através de uma tupla de 4 elementos inteiros, filtra apenas os inteiros pares
e retorna os elementos pares na mesma ordem na qual foram inseridos
    int+int+int+int -> int'''
    a=tup[0]%2
    b=tupla[1]%2
    c=tupla[2]%2
    d=tupla[3]%2
    
    if a==0 and b==0 and c==0 and d==0:
        return (tup[0],tup[1],tup[2],tup[3])
    elif b==0 and c==0 and d==0:
        return (tup[1],tup[2],tup[3])
    elif a==0 and b==0 and d==0:
        return (tup[0],tup[1],tup[3]) 
    elif a==0 and c==0 and d==0:
        return (tup[0],tupla[2],tup[3])
    elif a==0 and b==0 and c==0:
        return (tup[0],tupla[1],tup[2])
    elif a==0 and b==0 and d==0:
        return (tup[0],tupla[1],tup[3])
    elif a==0 and b==0 :
        return (tup[0],tup[1])
    elif a==0 and c==0:
        return (tup[0],tup[2])
    elif a==0 and d==0:
        return (tup[0],tup[3])
    elif b==0 and  c==0 :
        return (tup[1],tup[2])
    elif c==0 and d==0:
        return (tup[2],tup[3])
    elif d==0:
        return (tup[3],)
 
    else:
        return '()'