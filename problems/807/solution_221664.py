def conta_frases(frases):
    """Copia a string reccebi para outra e modifica as reticências, exclamações
    e interrogações para pontos finais. Retorna o comprimento da lista que separa
    as frases por pontos finais, e retira um pois a última string após o último ponto
    não é uma frase, é uma string vazia.
    str-> int"""
    frases_modificadas=frases
    frases_modificadas=frases_modificadas.replace("...",".")
    frases_modificadas=frases_modificadas.replace("!",".")
    frases_modificadas=frases_modificadas.replace("?",".")
    return len(frases_modificadas.split("."))-1