def faltante(lista):
    '''A função retornará o número que está quebrando uma sequência numérica
    dados de entrada -> list
    dados de saída -> int'''
    
    Q = len(lista)
    i = 0
    
    while i <= Q - 2:
        if lista[i] == lista[i+1] - 1:
            i = i + 1
            
        elif lista[-2] == lista[-1] - 1:
            return lista[-1] + 1
        
        return lista[i] + 1