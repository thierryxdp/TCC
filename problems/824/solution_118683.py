def uppCons(frase):
    '''
    Funçao que dado um frase, retorna a frase com somente as
    consoantes maiusculas
    str -> str
    '''
    m= frase
    i=0
    while i>len(frase):
        if frase[i] not in 'aeiouAEIOU':
            m= +str.upper(frase[i])
        i=i+1
    return m