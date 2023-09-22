def lingua_p(palavra):
    '''RECEBE UMA PALAVRA COMO PARAMETRO E RETORNA UMA NOVA PALAVRA TRADUZIDA PRA LINGUA DO P. STR-> STR'''
    minu=palavra.lower()
    novapalavra=''
    vogais='aeiouãáéíóú'
    for p in minu:
        novapalavra+=p
        if p in vogais:
            novapalavra += 'p' +p
    return novapalavra