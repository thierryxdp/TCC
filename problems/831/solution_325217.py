def lingua_p(palavra):
    '''traduz a palavra para a lingua do p
    string -> string'''
    palavra = str.lower(palavra)
    indice = 0
    novaFrase = ""
    while indice < len(frase):
        if frase[indice] not in 'aeiou
            novaFrase = novaFrase + (frase[indice])
            indice = indice + 1
        else:
            novaFrase = novaFrase + frase[indice] + "p"
            indice = indice + 1
    return novaFrase