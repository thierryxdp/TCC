def lingua_p(palavra):
    '''recebe uma palavra e a retorna traduzida na
    linguagem do p.
    str ->
    '''
    palavra_min = palavra.lower()
    palavra_p = ''
    vogais = 'aeiouáéíóúâêîôûãõà'
    for p in palavra_min:
        palavra_p += p
        if p in vogais:
            palavra_p += 'p' + p
    return palavra_p