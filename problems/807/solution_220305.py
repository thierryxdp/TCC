def conta_frases(texto):
    '''Retorna a quantidade de frases que aparecem no texto'''
    #string -> int
    Frase_ponto = texto.replace()
    Frase_exclamacao = texto.replace()
    Frase_interrogacao = texto.replace()
    Frase_reticencia = texto.replace()
    return (len(Frase_ponto) + len(Frase_exclamacao) + len(Frase_interrogacao) + len(Frase_reticencia))