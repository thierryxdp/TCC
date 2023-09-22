def insere(lista_numero,n):
    '''
    	Função que recebe como parâmetros 
        uma lista com números inteiros 
        ordenados e um número inteiro n,
        e retorna essa lista com o n 
        incluído, de forma que ela continue
        ordenada
        : param lista_numero: list
        : param n: int
        : return: list
    '''
    list.append(lista_numero,n)
    list.sort(lista_numero)
    
    return lista_numero