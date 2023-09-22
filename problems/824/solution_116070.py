def uppCons(texto):
    '''recebe como entrada uma frase e retorna a frase com todas as suas consoantes em maíusculas'''
    i=0
    texto_retorno = ''
    while i<len(texto):
        if texto[i] in 'bcdfghjklmnpqrstvxz':
           texto_retorno += str.upper(texto[i])
        else:
           texto_retorno += texto[i]
        i=i+1
    return texto_retorno