def uppCons (frase):
    '''recebe e retorna uma frase com todas as consoantes maiusculas
    str -> str'''
    
    i = 0
    upp = '' 
    
    while i < len(frase):
        if frase[i] in "bcdfghjklmpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
            upp = str.upper(frase[i])
        if frase[i] in "AEIOUaeiou":
            upp = str.lower(frase[i])
        i = i + 1
     
    return upp