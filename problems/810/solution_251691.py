def inverte(abc):

    #o comando split separa as palavras pelo espaço, transformando em lista, e então o comando .reverse inverte
    # as a lista (cada item da lista é uma palavra). o comando join junta novamente a lista e coloca um espaço entre
    # os itens.
    
    lista = str.split(abc)
    lista.reverse()
   
    abc = str.join(' ', lista)
    return abc