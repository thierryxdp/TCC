def retira_pontuacao(texto):
    """funcao que retira todos as pontuacoes(travessao, virgula, dois pontos e ponto e virgula, ponto final) e substitui por espaco
    str -> str"""
    texto = texto.replace("-"," ")
    texto = texto.replace(",", " ")
    texto = texto.replace(";", " ")
    texto = texto.replace(":", " ")
    texto = texto.replace(".", " ")
    texto = texto.replace("?", " ")
    texto = texto.replace("!", " ")
    return texto