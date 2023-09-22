def lingua_p(palavra):
    ''' '''
    for i in 'aeiouáéíóú':
        palavra = palavra.replace(i,i+'p'+i)
    return palavra