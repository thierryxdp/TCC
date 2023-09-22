# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Retorna a string com hashtag no incio meio e fim;
    str -> str"""
    meio = len(s)//2
    return "#" + str(s)[0:meio] + "#" + str(s)[meio:]  + "#"