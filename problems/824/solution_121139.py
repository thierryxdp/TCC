def uppCons(frase):
    '''str -> str'''
    '''retorna a frase com todas as consoantes maiusculas'''
    
    novaF = ''
    i = 0
    
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            novaF += frase[i].upper
            pass
        else:
            novaF += frase[i]
        i += 1
        pass
    return novaF