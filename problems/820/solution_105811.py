def posLetra(palavra,letra,n):
    '''A funcao recebe uma sentenca, uma letra e uma ocorrencia e retorna qual o indice
da enesima ocorrencia dessa letra str,str,int->int'''
    
    ordem=0
    string=list(palavra)
    
    if n>palavra.count(letra):
        return -1

    while string.count(letra)>1:
        if palavra[ordem]==letra:
            del string[ordem]
            string.insert(ordem,'θ')
        ordem=ordem+1
    return string.index(letra)