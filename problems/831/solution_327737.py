def lingua_p(palavra):
    """funcao que traduz uma palavra dada para a lingua do P;
    str->str"""
    palavra2=str.lower(palavra)
    novapalavra=''
    for i in palavra2:
        if i in 'aeiouáéúí':
            novapalavra=novapalavra+i+'p'+i
        else:
            novapalavra=novapalavra+i
    return novapalavra