def lingua_p(palavra):
    """Dado uma palavra, retoran ela traduzida na lingua do P. str -> str"""
    palavra = palavra.lower()
    vogal = 'aeiouàáâãêéíîóôõúû'
    auxiliar = ''
    i = 0
    while i < len(palavra):
        if palavra[i] in vogal:
            auxiliar += palavra[i] + 'p' + palavra[i]
        else:
            auxiliar += palavra[i]
        i += 1
    return auxiliar