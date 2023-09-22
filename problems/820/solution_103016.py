def posLetra(string,letra,ocorrencia):
    '''
	'''
    a = 0
    qtd_letra = str.count(string,letra)
    indice = -1
    
    if qtd_letra < ocorrencia:
        return -1
    elif qtd_letra > ocorrencia:
        while a < ocorrencia:
            indice = str.index(string,letra,indice + 1,len(string))
            a = a + 1
        return indice
    else:
        return str.index(string,letra)