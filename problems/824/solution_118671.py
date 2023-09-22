def uppCons(frase):
    '''
    Funçao que dado um frase, retorna a frase com somente as
    consoantes maiusculas
    str -> str
    '''
    
    i=0
    while i>len(frase):
        str.replace(frase,frase[i],str.upper(frase[i]))
        if frase[i] not in 'AEIOUaeiou':
            return frase
        i=i+1
    return frase