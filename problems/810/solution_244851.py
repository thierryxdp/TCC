def inverte(pontoExclamacao):
    """Funcao que dada uma frase retorne uma outra frase que contenha
        as mesmas palavras da frase de entrada na ordem inversa.
        str-->str"""
    travessao = pontoExclamacao.replace('-',' ')
    virgula = travessao.replace(',',' ')
    doisPontos = virgula.replace(':', ' ')
    pontoVirgula = doisPontos.replace(';', ' ')
    pontoFinal = pontoVirgula.replace('.', ' ')
    pontoInterrogacao = pontoFinal.replace('?', ' ')
    pontoExclamacao = pontoInterrogacao.replace('!', ' ')
    lista = str.split(pontoExclamacao)
    lista.reverse()
    frase = str.join(" ", lista)
    return pontoExclamacao