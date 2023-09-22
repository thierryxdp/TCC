def faltante(L):
    '''Função que ao receber uma lista com números representando as
    	peças de uma quebra-cabeças, retorna o número da peça em 
        falta
        
        list(int) -> int'''
    i = 1
    j = 0
    n = len(L) + 1
    l = []
    while i <= n:
        l = l + [1*i]
        i = i + 1
    while j < n:
        if l[j] not in L:
            return l[j]
        j = j + 1