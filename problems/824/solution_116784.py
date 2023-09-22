def consoantes (frase):

    prox = 0
    while prox <len(frase):
        if frase[prox] != 'a' and frase[prox] != 'e'and frase[prox] != 'i' and frase[prox] != 'o' and frase[prox] != 'u':
            return  str.upper(frase)[prox]