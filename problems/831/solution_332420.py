def lingua_p(palavra):
    vogais = ['a','e','i','o','u']
    lista_palavra = list(palavra)
    posicao = 0
    for letra in palavra:
        if letra in vogais:            
            list.insert(lista_palavra, posicao,'p')
            posicao += 1
        else:
            posicao += 1
    return lista_palavra