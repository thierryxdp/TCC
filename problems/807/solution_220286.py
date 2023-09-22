def conta_frases(texto):
    '''Retorna a quantidade de frases que aparecem no texto'''
    #string -> int
    Frase_ponto = texto.split('.') - texto.strip()
    Frase_exclamacao = texto.split('!') - texto.strip()
    Frase_interrogacao = texto.split('?') - texto.strip()
    Frase_reticencia = texto.split('...') - texto.strip()
    return (len(Frase_ponto) + len(Frase_exclamacao) + len(Frase_interrogacao) + len(Frase_reticencia))