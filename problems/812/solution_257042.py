def retira_pontuacao(frase):
    "Retorna a frase onde todos os caracteres de pontuação são substituidos por espaço. str->str"
    x = str.split(frase, ".")
    y = str.join(" ", x)
    return y