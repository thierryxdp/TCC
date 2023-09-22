def faltante(lista):
    '''A função retornará o número que está quebrando uma sequência numérica
    dados de entrada -> list
    dados de saída -> int'''
    
    Q = len(lista)
    i = 0
    
    while i < Q:
        if lista[i] != lista[i+1]+1:
            return lista[i] + 1
        i = i + 1