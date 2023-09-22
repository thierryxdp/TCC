def lingua_p(palavra):
    '''funcao que recebe uma palavra e traduz ela para a lingua do P; str -> str'''
    str.lower(palavra)
    indice = 0
    novastr = ''
    while indice <= len(palavra):
        if palavra[indice] in 'aeiouáéíóúâêîôûãõ':
            novastr = novastr + palavra[indice] + 'p' + palavra[indice]
        else:
            novastr = novastr + palavra[indice]
        i = i + 1
        return novastr