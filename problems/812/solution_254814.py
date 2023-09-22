def retira_pontuacao(frase):
    """Coloque um comentário dizendo o que a função faz e quais são 
    os parâmetros de entrada e saída
    str-> int"""
    
    if '-' or ',' or ':' or ';' or '.' or '?' or '!' in frase:
        return frase.replace(frase, " ")