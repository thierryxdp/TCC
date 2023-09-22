def retira_pontuacao(frase):
    """Coloque um comentário dizendo o que a função faz e quais são 
    os parâmetros de entrada e saída
    str-> int"""
    x= frase.replace(". ", " ") and frase.replace(", ", " ") 
    y=frase.replace("!", " ") and frase.replace("?", " ")
    return x and y