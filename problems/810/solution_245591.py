def inverte(frase):
    """Retorna a frase com as palavras na ordem inversa
    str->str"""
    travessao = frase.replace('-', ' ')
    virgula = travessao.replace(',', ' ')
    doisPontos = virgula.replace(':', ' ')
    pontoVirgula = doisPontos.replace(';', ' ')
    pontoFinal = pontoVirgula.replace('.', ' ')
    pontoInterrogacao = pontoFinal.replace('?', ' ')
    pontoExclamacao = pontoInterrogacao.replace('!', ' ')
    #reescrevi a função porque não consegui acessar a resposta
    frasespt= (pontoExclamacao)
    return frasespt[::-1]