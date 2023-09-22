def lingua_p(palavra):
    """funcao que traduz a palavra informada para a lingua do P

        str->str
    """
    vogais = "aeiouáéíóúâêîôûãõ"
    palavra = str.lower(palavra)
    lista_palavra = list(palavra)
    retorno = []
    
    for i in range(len(lista_palavra)):
        if lista_palavra[i] in vogais:
            list.append(retorno,lista_palavra[i])
            list.append(retorno,'p')
            list.append(retorno,lista_palavra[i])
        else:
            list.append(retorno,lista_palavra[i])
    return retorno