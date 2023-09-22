def filtra_pares(elementos):
    '''Função que recebe uma tupla com 4 elementos como parâmetro, e retorna uma tupla contendo apenas
    os elementos pares da tupla original em ordem sequencial
    tuple -> tuple'''

    a = elementos[0]%2
    b = elementos[1]%2
    c = elementos[2]%2
    d = elementos[3]%2

    if  a == 0 and b == 0 and c == 0 and d == 0:
        return (elementos[0], elementos[1], elementos[2], elementos[3])
    
    elif a == 0 and b == 0 and c == 0 and d != 0:
        return (elementos[0], elementos[1], elementos[2])
    
    elif a == 0 and b == 0 and c != 0 and d != 0:
        return (elementos[0],elementos[1])
    
    elif a == 0 and b != 0 and c != 0 and d != 0:
        return (elementos[0],)
    
    elif a == 0 and b != 0 and c == 0 and d != 0:
        return (elementos[0],elementos[2])
    
    elif a == 0 and b != 0 and c != 0 and d == 0:
        return (elementos[0],elementos[3])

    elif a == 0 and b != 0 and c == 0 and d == 0:
        return (elementos[0], elementos[2], elementos[3])
    
    elif a != 0 and b == 0 and c == 0 and d == 0:
        return (elementos[1], elementos[2], elementos[3])
    
    elif a != 0 and b == 0 and c == 0 and d != 0:
        return (elementos[1], elementos[2])
    
    elif a != 0 and b == 0 and c != 0 and d != 0:
        return (elementos[1],)

    elif a != 0 and b != 0 and c == 0 and d == 0:
        return (elementos[2], elementos[3])
    
    elif a != 0 and b != 0 and c == 0 and d != 0:
        return (elementos[2],)

    elif a != 0 and b != 0 and c != 0 and d == 0:
        return (elementos[3],)

    else:
        return ()