def lingua_p(palavra):
    """funcao que recebe como parametro uma palavra e retorna a mesma so que na lingua do P;
    str->str"""
    minusc=palavra.lower()
    novaPalavra=''
    vogais='aeiouãáéíóú'
    for p in minusc:
        novaPalavra+=p
        if p in vogais:
            novaPalavra+= 'p' + p
    return novaPalavra