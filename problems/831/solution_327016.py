def lingua_p(palavra):
    palavra = palavra.lower()
    vogal = 'aeiouàáâãêéíîóôõúû'
    auxiliar = ''
    i = 0
    while i < len(palavra):
        if palavra[i] in vogal:
            auxiliar += p[i] + 'p' + p[i]
            i += 1
        else:
            auxiliar += p[i]
            i += 1
    return auxiliar