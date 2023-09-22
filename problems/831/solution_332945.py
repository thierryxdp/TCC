def lingua_p(palavra):
    """Função que recebe como parâmetro uma palavra(em português) e retorna
    esta mesma palavra traduzida para a língua do P.
    str -> str"""
    minusc = palavra.lower()
    novaPalavra = ''
    vogais = 'aeiouãáéíóú'
    for p in minusc:
        novaPalavra += p
        if p in vogais:
            novaPalavra += 'p' + p

    return novaPalavra