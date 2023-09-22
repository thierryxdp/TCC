def lingua_p(palavra):
    """
    	Recebe uma palavra na língua portuguesa e retorna
        a palavra traduzida para língua do P.
    """
    vogais = "aeiouAEIOUáéíóúàèìòù"
    traducao = ""
    for letra in palavra:
        if letra not in vogais:
            traducao += letra
        else:
            traducao += letra + "p" + letra
    str.lower(traducao)
    return traducao