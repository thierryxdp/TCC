def uppCons(frase):
    '''função que retorne a frase com as consoantes em letras maiusculas da uma frase anterior com todas as letras em minusculo
    str->str'''
    proximo = 0
    Palavra=''
    while proximo<len(frase):
        if frase[proximo] in 'bcdfghjklmnpqrstvwxyzç':
            Palavra= Palavra + (str.upper(frase[proximo]))
        else:
            Palavra= Palavra + frase[proximo]
        proximo = proximo + 1
    return Palavra