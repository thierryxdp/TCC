def lingua_p(frase):
    acum=''
    for i in range(len(frase)):
        if frase[i] in 'aeiouáéíú':
            acum=acum+frase[i]+'p'+frase[i]
        else:
            acum=acum+frase[i]
    return acum