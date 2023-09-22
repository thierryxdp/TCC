def lingua_p(palavra):
    """
    str->str
    :param palavra: Pega a palavra de entrada e transforma para lingua p
    :param return: Retorna a palavra de entrada na lingua p
    """
    vogal = [a,e,i,o,u,á,é,ú,ã,õ,ê]
    nova_palavra = [ ]
    for letra in palavra:
        if letra in vogal:
            resposta = letra + "p" + letra
            list.append(nova_palavra,resposta)
        else:
            list.append(nova_palavra,letra)
    return str.join("",nova_palavra)