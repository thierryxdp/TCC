def posLetra(frase,letra,ocorrencia):
    ''' Função que, dada uma frase, uma letra presente na
    	frase e o numero da sua ocorrência, retorna o índice
        da letra nesta ocorrência dentro da frase. '''
    if str.count(frase, letra) > ocorrencia:
        return -1
    else:
        return str.index(frase,letra,ocorrencia)