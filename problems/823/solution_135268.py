def faltante(lista):
    '''
    	Função que recebe uma lista com
        N-1 inteiros numerados de 1 a N
        e retorna o número inteiro do 
        intervalo de 1 a N que está 
        faltando
        : param lista: list
        : return: int
    '''
    list.sort(lista)
    indice = 0
    
    if lista[0] != 1:
        return 1
    
    if lista[-1] == len(lista):
        return lista[-1] + 1
    
    while indice < len(lista):
        if lista[indice] + 1 != lista[indice+1]:
            return lista[indice] + 1
        indice += 1