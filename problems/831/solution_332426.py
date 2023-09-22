def lingua_p(palavra):
    consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l' , 'm', 'n', 'p'
    ,'q','r', 's', 't', 'v', 'x', 'y', 'w', 'z', 'ç']
    palavra = str.lower(palavra)
    lista_palavra = list(palavra)
    nova_lista = []
    for letra in palavra:
        if letra not in consoantes:
            list.append(nova_lista, letra)
            list.append(nova_lista, 'p')
            list.append(nova_lista, letra)
        else:
            list.append(nova_lista, letra)
    palavra_nova = str.join('',nova_lista)
    return palavra_nova