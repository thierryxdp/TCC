def insere(lista_numero, n, x=0):
    x = len(lista_numero)//2   
    if (n < (lista_numero[0])):
        return [n] + lista_numero
    
    elif n > (len(lista_numero)//2):
        return lista_numero[:x] + [n] 
    
    elif n > (len(lista_numero)-1):
        return lista_numero + [n]