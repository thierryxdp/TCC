def uppCons(frase):
    '''
    Funçao que dado um frase, retorna a frase com somente as
    consoantes maiusculas
    str -> str
    '''
    
    i=0
    frase=str.upper(frase)
    while i>len(frase):
        
        if frase[i] in 'AEIOUaeiou':
            #str.replace(frase,frase[i],str.lower(frase[i]))
            frase=frase+str.replace(frase,frase[i],str.lower(frase[i]))
        i=i+1
    return frase