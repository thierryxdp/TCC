def filtraMultiplos(lista,n):
        '''
        funcao que recebe uma lista e um numero n, e verifica
        se os itens da lista sao divisiveis por n, e os retorna
        em uma lista
        lista, int -> lista
        '''
        
        lista1 = []
        i = 0
        while (i<len(lista)):
        	if lista[i] % n == 0:
            lista1.append(i)
            i = i + 1 
            return lista1