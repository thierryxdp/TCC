insere(lista_numero, n):
        """ Função que dada uma lista ordenada(crescente) de números inteiros, e um número inteiro n, inclui n na posição correta, de modo que a lista continue ordenad
        """
        lista_numero.append(n)
    	lista_numero.sort()
    
    	return lista_numero