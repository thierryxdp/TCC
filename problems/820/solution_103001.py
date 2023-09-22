def posLetra(string,letra,ocorrencia):
    '''
	'''
	indice = 0
    a = 0
    qtd_letra = str.count(string,letra)
    
    if qtd_letra < ocorrencia:
        return -1
    elif qtd_letra > ocorrencia:
        while a < ocorrencia or ocorrencia == 1:
            a = str.index(string,letra,a,len(string))
        a = a + 1  
        return a
    else:
        return str.index(string,letra)