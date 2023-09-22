def lingua_p(palavra):
    """ Traduz a palavra para a língua do P.
    	string -> string
        
        Parameter:
        palavra: Palavra a ser traduzida.
        
        Returns:
        Palavra na língua do P.
    """
    lista = list(palavra)
    lista2 = []
    vogais = list('aáeéiíoóuú')
    for letra in lista:
        if letra not in vogais:
            lista2.append(letra)
        elif letra in vogais:
            lista2.append(letra)
            lista2.append('p')
            lista2.append(letra)
    return str.join('', lista)