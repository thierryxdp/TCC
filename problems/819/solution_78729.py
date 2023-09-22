def filtraMultiplos(numeros:tuple,x):
    """Função que filtra os multiplos de um número n , tuple-->tuple"""
    lista=[] 
    n=0
    while n < len(numeros):
        if x % numeros[n] == 0 :
            list.append(lista,numero[x])
        n=n+1
    return lista