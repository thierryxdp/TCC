def inverte(frase):
    texto = retira_pontuacao(frase)
    minuscula = str.lower(texto)
    return str.join(' ' ,str.split(minuscula,' ')[::-1]