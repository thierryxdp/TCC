def faltante(lista):
    '''funcao que dado uma lista com N-1
    numeros retorna qual numero esta
    faltando; list -> int'''
    
    i = 0
    L = list.sort(lista)
    todasPecas = range(1,len(lista)+2)
    
    while i < len(lista):
        if L[i] != todasPecas[i]:
            i = i +1
    return i