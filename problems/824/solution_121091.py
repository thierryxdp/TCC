def uppCons(frase):
    """ Recebe uma frase como entrada e retorna toda a frase com as consoantes em letra maioscula. 
    assinatura: str --> str"""
    finaal = ''
    num = 0 
    while num < len (frase): 
        if: frase [num] in "bcdfghjklmnpqrstvwxyzç"
           final += str.upper (frase [num] ) 
        else: 
            final += frase [num] 
        num += 1
    return final