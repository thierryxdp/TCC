def uppCons(frase):
    '''str -> str'''
    '''retorna a frase com todas as consoantes maiusculas'''
    
    novaF = str()
    i = 0
    
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyzç':
            novaF += str.upper(frase[i])
            pass
        
        else:
            novaF += frase[i]
        i += 1
        pass
    
    return novaF