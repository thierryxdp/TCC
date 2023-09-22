def inverte(texto):
    texto = retira_pontuacao(texto)
    texto = str.split(texto)
    texto = texto[: :-1]
    texto = str.join(' ',texto)
    return texto