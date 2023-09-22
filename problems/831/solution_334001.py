def lingua_p(palavra):
    """Função que recebe como parâmetro um apalavra(em português) e retorna esta mesma palavra traduzida para a língua do P.
    str -> str"""
    minusc = palavra.lower()
    novaPalavra = ''
    vogais = 'aeiouãáéíóú'
    for p in minusc:
        novaPlavra += p
        if p in vogais:
            novaPlavra += 'p' + p
            
            return novaPalavra