def faltante(lista):
    '''funcao que dado uma lista com N-1
    numeros retorna qual numero esta
    faltando; list -> int'''
    
    i = 0
    todasPecas = list(range(1,len(lista)+2))
    N = max(lista)
    
    if lista[:] == todasPecas[:N]:
        return todasPecas[-1]
    
    else:
        while todasPecas[i] == lista[i]:
            i = i + 1
        return todasPecas[i]