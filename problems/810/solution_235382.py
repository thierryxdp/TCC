def inverte(frase):
    '''Funcao que, dada uma frase, retorna uma outra frase que contenha as mesmas palavras da frase na ordem inversa, sem letras maiusculas e pontuação.'''
    ''' str -> str'''

    ponto = frase.replace ('.',' ')
    virgula = ponto.replace (',',' ')
    exclamacao = virgula.replace ('!',' ')
    interrogacao = exclamacao.replace ('?',' ')
    dois_pontos = interrogacao.replace (':',' ')
    ponto_virgula = dois_pontos.replace (';',' ')
    travessao = ponto_virgula.replace('-',' ')
    travessao = str.lower(travessao)
    lista = str.split(travessao, " ")
    travessao = str.join(" ", lista)
    travessao = str.strip (travessao)
    return travessao.reverse ()