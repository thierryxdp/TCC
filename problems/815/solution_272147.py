def insere(lista_numero,n):
    '''
    	Função que dada uma lista ordenada de numeros crescentes retorna uma nova lista incluindo um numero n e continue ordenada
        list -> list
    '''
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero