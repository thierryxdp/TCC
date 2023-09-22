def retira_pontuacao(frase):
    """funcao que, dada uma frase, retorna a frase em que todos
    os caracteres de pontuacao (travessao, virgula, dois pontos, ponto
    e virgula, etc) tenham sido substituidos por espaco
    str -> str"""
    lista = str.split(frase,',','.') or lista = str.split(frase,'?','!')
    frase = str.join(' ',lista)
    return frase