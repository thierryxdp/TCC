def posLetra(string,letra,ocorrencia):
    '''
    	Função que recebe como parâmetros 
        de entrada uma string, uma letra
        e um número que indica a ocorrência
        desejada da letra, e retorna em que 
        posição da string a ocorrência da
        letra está e, caso existam menos
        ocorrências da letra do que a
        ocorrência pedida, é retornado -1
        : param string: str
        : param letra: str
        : param ocorrencia: int
        : return: int
    '''
    if str.count(string,letra) < ocorrencia:
        return -1
    
    contador = 1
    posicao = str.index(string,letra)
    
    while contador < ocorrencia:
        posicao += 1
        posicao = str.index(string,letra,posicao)
        contador += 1
        
    return posicao