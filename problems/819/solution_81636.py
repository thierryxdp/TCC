def filtraMultiplos(lista,n):
        '''
        funcao que recebe uma lista e um numero n, e verifica
        se os itens da lista sao divisiveis por n, e os retorna
        em uma lista
        lista, int -> lista
        '''
        
        lista1 = []
        contador = 0
        while (contador < len(lista)):
        	if lista[contador] % n == 0:
            	lista1.append(contador)
            contador = contador +1
        return lista1