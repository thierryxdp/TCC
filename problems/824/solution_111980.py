def uppCons(frase):
    '''
    string --- > string
    deixa as letras consoantes da frase recebida em minusculas
    '''
    frase_final = ''
    i=0
    while i < len(frase):
        if frase[i] in 'çbcdfghjklmnpqrstvxzwkyBCDFGHJKLMNPQRSTVXZWKY':
            frase_final += frase[i].upper()
        else:
            frase_final += frase[i]
        i+=1
    return frase_final