def conta_frases(texto):
    '''Função que recebe um texto armazenado em uma string e que retorna 
    a quantidade de frases contidas no texto
    str => int'''
    ponto=texto.count(".")
    exclamacao=texto.count("!")
    interrogacao=texto.count("?")
    reticencias=texto.count("...")
    pontos=ponto+exclamacao+reticencias+interrogacao
    if reticencias >= 1:
        return pontos - reticencias*3
    return pontos