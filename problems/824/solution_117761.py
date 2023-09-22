def uppCons(frase):
    ''' funçaõ que recebe um frase e retorna outra frase com consoantes maiusculas; str->str'''
    i = 0
    
    a=''
    
    while i < len(frase):
        if frase[i].lower() in 'qwrtypsdfghjklçzxcvbnm':
            a+=frase[i].replace(frase[i], frase[i].upper()) 
        else:
            a+= frase[i]
        i+=1
       
    return a