def uppCons(frase):
    """A funçao com uma string de entrada retornara uma outra string com as 
    consoantes da frase incial em letra maiuscula.str-->str """
    lista = list(range(len(frase)))
    lista[:] = frase
    i = 0
    while i < len(lista):
        if frase[i] in "bcçdfghjklmnpqrstvwxzy ":
            lista[i] = str.upper(lista[i])
        i = i + 1
    return str.join("",lista)