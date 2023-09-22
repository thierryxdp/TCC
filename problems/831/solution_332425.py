def lingua_p(palavra):
    vogais = ['a','e','i','o','u']
    lista_palavra = list(palavra)
    nova_lista = []
    for letra in palavra:
        if letra in vogais:
            list.append(nova_lista, letra)
            list.append(nova_lista, 'p')
            list.append(nova_lista, letra)
        else:
            list.append(nova_lista, letra)
    palavra_nova = str.join('',nova_lista)
    return palavra_nova