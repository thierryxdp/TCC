def conta_frases(frases):
    '''
    funcao que dada uma frase, conta quantos pontos de interrogaçao,
    exclamaçao, tres pontos em sequencia (equivale a uma reticencias)
    tem no total ou um ponto final. 
    Lembrando que pontos de exclamaçao ou de interrogaçao nao
    aparecerao repetidos em sequencia no texto e esses simbolos so
    aparecem no texto terminando uma frase.
    :param frases: str
    :return: int
    '''
    ponto_final = frases.replace("...", '@')
    ponto_exclamacao = ponto_final.replace("!", '@')
    ponto_interrogacao = ponto_exclamacao.replace("?", '@')
    reticencias = ponto_interrogacao.replace(".", '@')
    return reticencias.count('@')