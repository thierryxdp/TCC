def uppCons(frase):
    '''
    Funçao que dado um frase, retorna a frase com somente as
    consoantes maiusculas
    str -> str
    '''
    
    i=0
    while i>len(frase):
        m=str.upper(frase)
        if frase[i] in 'AEIOUaeiou':
            #str.replace(frase,frase[i],str.lower(frase[i]))
            m=frase+str.replace(frase,frase[i],str.lower(frase[i]))
        i=i+1
    return m