def uppCons (frase):

    prox = 0
    while prox <len(frase):
        if frase[prox] != 'a' and 'e'and 'i' and 'o' and 'u':
            return  str.upper(frase)