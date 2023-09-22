def faltante(lista):
    '''Função que, dada uma lista com N-1 inteiros numerados de 1 a N, retorna o número inteiro que está faltando.
    list -> int'''
    list.sort(lista)
    proximo = 0 
    peca = 1
    while proximo <len(lista) and peca < len(lista):
        if lista [proximo] - lista[peca] == -2:
            return lista[proximo] + 1
    	proximo = proximo + 1
    	peca = peca + 1
    if lista [0] == 2:
        return 1
    else: 
        return lista[proximo]+1