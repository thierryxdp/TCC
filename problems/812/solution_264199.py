def retirar_pontuacao(pontuacao):
    """ funcao que dada uma palavra retire a
    pontuacao da palavra """
    sinais = [",", '.', '-', ':', '!', '?']
    palavras = pontuacao
    for sinal in sinais:
        palavra = palavra.replace(sinal,' ')