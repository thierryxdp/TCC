def inverte(frase):
    """ essa função alem de tirar todos os sinais de pontuação, ainda inverte as palavras na ordem inversa sem letras maiusculas
    entrada -> str
    saida -> str """
    frase = retira_pontuacao(frase)
    frase2 = str.split(frase)
    frase3 = frase2[::-1]
    return str.join(" ", frase3)