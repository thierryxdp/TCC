def uppCons(frase:str) -> str:
    '''retorna a frase dada com todas suas consoantes em maiúscula'''
    cons = ''
    for caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvxwyzç':
            cons += caractere.upper()
        else:
            cons+= caractere
    return cons