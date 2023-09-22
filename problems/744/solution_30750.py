# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """
    Essa função recebe uma string 's' e retorna a string com '#' no 
    início, no meio e no final dela;
    """
    return "#" + s[:len(s)//2] + "#" + s[:len(s)] + "#"