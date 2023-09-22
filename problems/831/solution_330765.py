def lingua_p(frase):
    '''função que recebe uma palavra em português e retorna
    a mesma palavra traduzida pra língua do P'''
    acum=''
    for i in range(len(frase)):
        if frase[i] in 'aeiouáéíú':
            acum=acum+frase[i]+'p'+frase[i]
        else:
            acum=acum+frase[i]
    return acum