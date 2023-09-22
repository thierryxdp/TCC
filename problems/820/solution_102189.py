def posLetra(string,letra,num): 
    ''' Função que recebe como entrada uma string, uma letra
        e um numero. A função deve retornar em que posição da
        string aquela ocorrencia está. 
        : param string: str
        : param letra: str
        : param num: int
        : return: int
    '''
    i=0
    ocorrencia=0
    while i<len(string):
        if string[i]==letra:
            ocorrencia=ocorrencia+1
        if ocorrencia==num:
            return i
        i=i+1
    return -1