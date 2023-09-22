def uppCons (frase):
    '''recebe e retorna uma frase com todas as consoantes maiusculas
    str -> str'''
    
    i = 0
    upp = '' 
    
    while i < len(frase):
        if frase[i] in "bcdfghjklmpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
            upp = upp + str.upper(frase[i])
        else:
            upp = upp + frase[i]
        i = i + 1
     
    return upp