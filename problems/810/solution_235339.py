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
    lista = str.split(travessao, "")
    lista.reverse()
    travessao = str.join(" ", lista)
    travessao = str.lower(travessao)
    return travessao