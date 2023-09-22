def retira_pontuacao(frase):
    """Coloque um comentário dizendo o que a função faz e quais são 
    os parâmetros de entrada e saída
    str-> int"""
    return frase.replace(".", " ") or frase.replace(",", " ")