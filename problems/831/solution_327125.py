def lingua_p(palavra):
    """ Traduz a palavra para a língua do P.
    	string -> string
        
        Parameter:
        palavra: Palavra a ser traduzida.
        
        Returns:
        Palavra na língua do P.
    """
    lista = list(palavra)
    vogais = list('aeiouAEIOU')
    for vogal in vogais:
        if vogal in lista:
            lista.insert(lista.index(vogal), 'p')
            lista.insert(lista.index(vogal) + 1, vogal)
    return str.join('', lista)