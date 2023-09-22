def filtraMultiplos(numeros:tuple,x):
    """Função que filtra os multiplos de um número n , tuple-->tuple"""
    lista=[] 
    n=0
    while n < len(numeros):
        if x % n  == 0 :
            list.append(lista,x)
        n=n+1
    return lista