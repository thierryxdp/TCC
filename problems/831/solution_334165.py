def lingua_p(palavra):
    """ funçao que recebe uma palavra como entrada e retorna essa mesma palavra traduzida 
    	para a lingua do P. str --> str  """
    
    vogais = "aeiouAEIOUáéíóúàèìòù"
    traducao = ""
    for letra in palavra:
        if letra not in vogais:
            traducao += letra
        else:
            traducao += letra + "p" + letra
    str.lower(traducao)
    return traducao