def retira_pontuacao(frase):
    pontos = [".", "?", "!", "...", ",", "-", ":", ";"]
    lista = list(frase)
    index = 0
    for letra in frase:
        if letra in pontos:
            lista[index] = " "
        else:
            lista[index] = letra
        index = index + 1
    word = ''.join(lista)
    return word