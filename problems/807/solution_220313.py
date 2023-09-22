def conta_frases(texto):
    '''Retorna a quantidade de frases que aparecem no texto'''
    #string -> int
    Frase_ponto = texto.split('.')
    Frase_exclamacao = texto.split('!')
    Frase_interrogacao = texto.split('?')
    Frase_reticencia = texto.count('...')
    return (len(Frase_ponto) - 2*(Frase_reticencia) + len(Frase_exclamacao) + len(Frase_interrogacao) + len(Frase_reticencia)-3)