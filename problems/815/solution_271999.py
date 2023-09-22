def insere(lista_numero, n, x=0):
    x = len(lista_numero)//2
    if (n < (lista_numero[0])):
        return [n] + lista_numero
    
    elif lista_numero[0] < n < lista_numero[x]:
        return lista_numero[:x] + [n] + lista_numero[x:]