def faltante(lista):
    
    """Dada uma lista com numeros inteiros diferentes, retorna 
    os numeros pertencentes ao intervalo entre 1 e N. list -> int """
    i = 0
    lst_return = []
    while lista[i] < len(lista):
        if lista[i + 1] != lista[i] +1:
            lst_return.append(lista[i] + 1)
         
    return lst_return