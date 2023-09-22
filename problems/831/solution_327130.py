def lingua_p(palavra):
    """ Traduz a palavra para a língua do P.
    	string -> string
        
        Parameter:
        palavra: Palavra a ser traduzida.
        
        Returns:
        Palavra na língua do P.
    """
    lista = list(palavra)
    vogais = list('aáeéiíoóuú')
    for letra in lista:
        if letra in vogais:
            lista.insert(lista.index(letra) + 1, 'p')
            lista.insert(lista.index(letra) + 2, letra)
    return str.join('', lista)