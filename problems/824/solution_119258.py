def uppCons(frase):
    '''Retorna uma string com as consoantes de 'frase' em maíusculo.
    Assinatura: string->string'''
    string = ''
    for x in frase:
        if x in 'bcdfghjklmnpqrstvwxyzç':
            string+=x.upper()
        else:
            string+=x
    return string