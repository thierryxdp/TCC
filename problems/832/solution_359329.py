def eh_quadrada(A):
    numero=len(A)
    lista=['']
    for elem in range(numero):
        if '' in lista:
            numero2=len(A[elem])
            list.append(lista,numero2)
            list.remove(lista,'')
        else:
            numero2=len(A[elem])
            list.append(lista,numero2)
    if sum(lista)==(len(A)*A[0]):
        return True
    elif lista==['']:
        return True
    else:
        return False