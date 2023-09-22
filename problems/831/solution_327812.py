def lingua_p(palavra):
    '''Retorna uma palavra dado como entrada traduzida para a língua do P;
    str -> str'''
    for c in 'AEIOUaeiou':
        palavra = str.replace(palavra,c,c+'p'+c)
    return palavra.lower()