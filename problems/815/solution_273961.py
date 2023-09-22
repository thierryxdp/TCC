def insere(lista_numero, n):
    '''
    	Funcao que recebe uma lista ordenada de numeros inteiros
        e um numero inteiro, e retorna o numero n incluido na 
        posicao correta
        list, int -> list
    '''
    lista_numero.insert(0, n)
    list.sort(lista_numero)
    return lista_numero