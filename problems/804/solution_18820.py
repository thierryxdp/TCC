def filtra_pares(tupla_inteiros):
    	'''
        Função que filtra os números pares dentro de um conjunto de números recebidos.
        Valor de entrada do tipo tupla (int)
        Valor de retorno do tipo tupla (int)
        '''
        n1, n2, n3, n4 = tupla_inteiros[0], tupla_inteiros[1], tupla_inteiros[2], tupla_inteiros[3]
        nova_lista = []
        if n1%2 == 0:
	        nova_lista.append(n1)
        if n2%2 == 0:
	        nova_lista.append(n2)
        if n3%2 == 0:
	        nova_lista.append(n3)	
        if n4%2 == 0:
                nova_lista.append(n4)

        return tuple(nova_lista)