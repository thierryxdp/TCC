def conta_frases(frase):
    '''funcao que calcula a quantidade de pontos finais, exclamacoes
       interrogacoes e reticencias que aparecem na frase
       frase: str
       return: int
    '''
    pontoFinal = frase.replace("...", '#')
    exclamacao = pontoFinal.replace("!", '#')
    interrogacao = exclamacao.replace("?", '#')
    reticencias = interrogacao.replace(".", '#')
    return reticencias.count('#')