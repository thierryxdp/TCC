def faltante(lista):
    '''funcao que dado uma lista com N-1
    numeros retorna qual numero esta
    faltando; list -> int'''
    
    i = 0
    N = max(lista)
    todasPecas = list(range(1,len(lista)+2))
    
    while todasPecas[i] == lista[i]:
        i = i + 1
    return a[i]