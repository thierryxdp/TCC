def lingua_p(palavra):
    '''adiciona uma letra p apos cada vogal
    :param palavra: str->str
    :return: str->str
    '''
    minusculo = palavra.lower()
    novapalavra = ''
    vogais = 'aeiouãáéíóú'
    for p in minusculo:
        novapalavra += p
        if p in vogais:
            novapalavra += 'p' + p
    return novapalavra