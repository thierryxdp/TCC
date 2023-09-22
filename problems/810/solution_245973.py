def inverte (frase):
    teste = retira_pontuacao(frase)
    frase = str.split(frase)
    teste = str.split(teste)
    list.reverse(teste)
    teste = str.lower(' '.join(teste))
    return teste