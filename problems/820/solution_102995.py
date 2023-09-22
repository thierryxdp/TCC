def posLetra(string,letra,ocorrencia):
    '''
	função que recebe uma string, uma letra e um número que indica a ocorrencia desejada da letra e retorna em que posição da string aquela ocorrencia está;
    str,str,int->int
    '''
    indice = 0
    a = 0
    qtd_letra = str.count(string,letra)
    
    if qtd_letra < ocorrencia:
        return -1
    elif qtd_letra > ocorrencia:
        while a < ocorrencia:
            indice = str.index(string,letra,a,len(string))
        a = a + 1  
        return indice
    else:
        return str.index(string,letra)