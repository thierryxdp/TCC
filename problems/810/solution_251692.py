def inverte(frase):

    #o comando split separa as palavras pelo espaço, transformando em lista, e então o comando .reverse inverte
    # as a lista (cada item da lista é uma palavra). o comando join junta novamente a lista e coloca um espaço entre
    # os itens.
    
    frase = str.split(frase,'-')
    frase = str.join(' ',frase)
    frase = str.split(frase,',')
    frase = str.join(' ',frase)
    frase = str.split(frase,':')
    frase = str.join(' ',frase)
    frase = str.split(frase,';')
    frase = str.join(' ',frase)
    frase = str.split(frase,'.')
    frase = str.join(' ',frase)
    return frase

    
    
    lista = str.split(frase)
    lista.reverse()
   
    frase = str.join(' ', lista)
    return frase