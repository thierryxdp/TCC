# Retorna a string de entrada com '#' no início,meio e fim
# st=string de entrada,divisao=divisão do comprimento da string por 2
# str-> str
def hashtag(s):
    divisao=len(s)//2
    return '#'+s[:divisao]+'#'+s[divisao:]+'#'