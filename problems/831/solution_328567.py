def lingua_p(palavra: str)-> str:
    """ Traduz uma palavra da língua portuguesa para a língua do P,
    ignorando diferença entre maiúsculas e minúsculas."""
    
    palavra = str.lower(palavra)
    letras = list(palavra)
    i = 0

    while (i < len(letras)):
        if (letras[i] in 'aeiouáàâãéêóôõíú'):
            list.insert(letras, i+1,'p' + letras[i])
        i += 1

    return str.join('',letras)