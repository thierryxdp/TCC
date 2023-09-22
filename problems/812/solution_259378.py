def retira_pontuacao(frase):
    pontuacao = ['-', ',', ':', ';', '.']
    frase_f = []
    lista = frase.split()
    lista_f = list(map(frase_f.append if lista not in pontuacao, lista))
    return lista_f.join()