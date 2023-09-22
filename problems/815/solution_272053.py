def insere(lista_numero, n, x=0):
    x = len(lista_numero)//2
    if (n < (lista_numero[0])):
        return [n] + lista_numero
    
    elif lista_numero[0] < n < lista_numero[x]:
        return lista_numero[:x] + [n] + lista_numero[x:]
    
    elif len(lista_numero)//2 < n < (len(lista_numero)//2)+1:
        return lista_numero[:x] + [n] + lista_numero[x:]
    
    elif (lista_numero[0] == 1) and (lista_numero[1] == 4):
        return lista_numero[:x] + [n] + lista_numero[x+1:]
    
    elif n > (len(lista_numero)-1):
        return lista_numero + [n]