def insere(lista_numero, n):
    '''Funcao que dada uma lista e um numero inteiro n,
    inclue n na posicao correta e retorna essa lista
    Parametros:
    list, int
    Saida: list
    '''
    
    l= lista_numero + [n]
    
    
    return sorted(l)