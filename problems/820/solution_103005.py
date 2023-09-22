def posLetra(string,letra,ocorrencia):
    '''
	'''
    a = 0
    qtd_letra = str.count(string,letra)
    
    if qtd_letra < ocorrencia:
        return -1
    elif qtd_letra > ocorrencia:
        while indice < qtd_letra:
            indice = str.index(string,letra,indice,len(string))
        indice = indice + 1  
        return indice
    else:
        return str.index(string,letra)