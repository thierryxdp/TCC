def repetidos(lista):
    '''Função que dada uma lista de números, irá retornar o número de vezes que um elemento é igual ao anterior. list -> int'''
    rep=0
    i=1
    while i<len(lista):    	
        if lista[i-1]==lista[i]:
            rep=rep+1
    	i=1+i      
    return rep