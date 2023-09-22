def posLetra(frase,referente,indice):
    n = 0
    frase1 = ''
    while n<len(frase) and str.count(frase1,referente) <= indice:
        if str.count(frase1,referente) == indice:
           r = len(frase1)
        n = n + 1
        frase1 += frase[n]
    return  r