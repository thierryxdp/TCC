def uppCons(frase):
    '''
    Funçao que dado um frase, retorna a frase com somente as
    consoantes maiusculas
    str -> str
    '''
    m=''
    i=0
    while i>len(frase):
        if frase[i] not in 'AEIOUaeiou':
            m=str.replace(frase,frase[i],str.upper(frase[i]))
            return m
        i=i+1
    return m