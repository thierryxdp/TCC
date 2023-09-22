def filtraMultiplos(numeros:tuple,x):
    """Função que filtra os multiplos de um número n , tuple-->tuple"""
    lista=[] 
    n=numeros   
    while n in numeros:
        if n % x  == 0:
            list.append(lista,n)   
    return lista