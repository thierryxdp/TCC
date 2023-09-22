def maiores(lista_numero,n):
    '''
    Parametros: lista_numero ->sequencia numerica
    			n            ->outro numero
    entrada   : lista, int
    saída     : lista
    
    Função que dada uma lista ordenada de numeros inteiros e um numero, retorna uma sequencia numerica decrescente
    
    
    '''
    nova_lista = lista_numero +  [n]
    nova_lista.sort(reverse = True)

    return nova_lista