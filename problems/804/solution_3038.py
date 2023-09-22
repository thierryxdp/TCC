def filtra_pares(tupla):
    '''funçao que possui quatro elementos inteiros como parâmetro e retorna os elementos pares'''
    a=tupla[0]%2
    b=tupla[1]%2
    c=tupla[2]%2
    d=tupla[3]%2
    if a==0 and b==0 and c==0 and d==0:
        return (tupla[0],tupla[1],tupla[2],tupla[3])
    elif a==0 and b==0 and c==0 and d!=0:
        return (tupla[0],tupla[1],tupla[2])
    elif a==0 and b!=0 and c==0 and d!=0:
        return (tupla[0],tupla[2])
    elif a==0 and b==0 and c!=0 and d!=0:
        return (tupla[0],tupla[1])
    elif a!=0 and b!=0 and c!=0 and d==0:
        return (tupla[3],)
    elif a==0 and b!=0 and c==0 and d==0:
        return (tupla[0],tupla[2],tupla[3])
    elif a!=0 and b!=0 and c!=0 and d!=0:
        return ()
    elif a!=0 and b!=0 and c==0 and d==0:
        return (tupla[2],tupla[3])
    elif a!=0 and b==0 and c==0 and d!=0:
        return (tupla[1],tupla[2])
    elif a!=0 and b==0 and c==0 and d==0:
        return(tupla[1],tupla[2],tupla[3])