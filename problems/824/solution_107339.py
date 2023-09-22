def uppCons(frase):
    '''A função recebe uma frase de entrada e retorna ela com todas as suas consantes sendo maiúsculas e os demais caracteres retorns normalmente
    str->str'''
    
    frasederetorno = ''
    comprimento = 0
    consoantes = 'bfjmnprstcdgklqvwxz'
    while comprimento < len(frase):
        if frase[comprimento] in consoantes:
            frasederetorno = frasederetorno + (str.upper(frase[comprimento]))
        else:
            frasederetorno = frasederetorno + frase[comprimento]
        comprimento = comprimento + 1
     return frasederetorno