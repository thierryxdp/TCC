def uppCons(texto):
    '''
        Função que retorna a frase com todas as suas consoantes em letras maiúsculas;
        string => string
    '''
    i=0
    texto = list(texto)
    while i<len(texto):
        if texto[i].upper() in 'BHCDFGJKLMNPQRSTVWXYÇZ':
            texto[i] = texto[i].upper()
        i=i+1
    texto = ''.join(texto)
    return texto