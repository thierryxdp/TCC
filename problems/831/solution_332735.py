def lingua(palavra):
    """ volta a palavrana lingua do P str > str"""
    vogais = 'aeiouAEIOU'
    c = len(palavra)
    i = 0
    while i < len(palavra) :
        if palavra[i] in vogais :
            substring = palavra[i] + 'p' + palavra[i]
            palavra.replace(palavra[i],substring)
            i = i + 3
        else:
            i = i + 1
    return palavra