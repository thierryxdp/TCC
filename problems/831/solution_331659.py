def lingua_p(palavra):
    '''Função que recebe uma palavra (em português) e retorna essa
palavra traduzida para a língua do P;
    str -> str'''
    p=''
    str.lower(palavra)
    for elemento in range(len(palavra)):
        if palavra[elemento] in 'aeiouáéíóúãõà':
            p=p+palavra[elemento]+'p'+palavra[elemento]
        else:
            p=p+palavra[elemento]
    return p