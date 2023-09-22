def filtra_pares(tupla):
    ''' 
    Função que, dada uma tupla com 4 elementos inteiros,
    retorna uma nova tupla apenas com os elementos pares,
    na mesma ordem da tupla original.
    Parâmetros:
    	tupla: Tuple
    Saída:
    		Tuple
    '''
    nova_tupla = ()
    if tupla[0]%2 == 0:
        nova_tupla = nova_tupla + (tupla[0],)
    if tupla[1]%2 == 0:
        nova_tupla = nova_tupla + (tupla[1],)
    if tupla[2]%2 == 0:
        nova_tupla = nova_tupla + (tupla[2],)
   	else tupla[3]%2 == 0:
        nova_tupla = nova_tupla + (tupla[3],)
        return nova_tupla