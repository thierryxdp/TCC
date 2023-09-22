def filtra_pares(tupla):
    '''função que recebe uma tupla com 4 elementos inteiros e
    retorna uma nova tupla apenas com os elementos pares,
    na mesma ordem
    tupla -> tupla'''
    elementos_pares = []
    for item in tupla :
        if item%2==0 :
          elementos_pares.append(item) 
    return tupla(elementos_pares)