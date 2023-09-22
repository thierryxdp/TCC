def retira_pontuacao(frase):
    pontuacao = ['-', ',', ':', ';', '.']
    frase_f = []
    lista = frase.split()
    a = list(map(lambda x: frase_f.append() if x not in pontuacao, lista))
    return a