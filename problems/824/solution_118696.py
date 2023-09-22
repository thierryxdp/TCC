def uppCons(frase):
    '''
    Funçao que dado um frase, retorna a frase com somente as
    consoantes maiusculas
    str -> str
    '''
    m= ''
    i=0
    while i<len(frase):
        if frase[i] not in 'aeiouAEIOU':
            m= frase+str.upper(frase[i])
        else:
            m=frase+frase[1]
        i=i+1
    return m