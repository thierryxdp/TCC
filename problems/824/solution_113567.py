def uppCons (frase):
    '''funcao que retorna frase com todas as consoantes maiusculas'''
    s = ''
    for caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvxwyzç':
            s += caractere.upper() # transforma em maiúscula
        else: # não é consoante minúscula, mantém como no original
            s += caractere
    return s