def uppCons(frase):
    '''
    Funçao que dado um frase, retorna a frase com somente as
    consoantes maiusculas
    str -> str
    '''
    m=''
    i=0
    frase=str.upper(frase)
    while i>len(frase):
        
        if frase[i] in 'aeiou':
            str.replace(frase,frase[i],str.lower(frase[i]))
            m=str.replace(frase,frase[i],str.lower(frase[i]))
        i=i+1
    return frase