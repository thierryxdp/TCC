def uppCons(frase):
    '''função que retorna a frase com todas as suas consoantes
    em maiúsculas
    str -> str'''
    nova_frase = ''
    i = 0
    while i < len(frase):
        if frase[i] not in 'AEIOUaeiouÃãáàâíôõ':
            nova_frase = nova_frase + str.upper(frase[i])
        else:
            nova_frase = nova_frase + frase[i]
        i += 1
    return nova_frase