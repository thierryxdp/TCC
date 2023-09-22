def lingua_p(palavra):
    vogais = ['a','e','i','o','u']
    lista_palavra = list(palavra)
    posicao = 0
    for letra in palavra:
        if letra in vogais:            
            list.insert(lista_palavra, posicao + 1,'p')
            list.insert(lista_palavra, posicao + 2, letra)
            posicao += 1
        else:
            posicao += 1
    palavra_nova = str.join('',lista_palavra)
    return palavra_nova