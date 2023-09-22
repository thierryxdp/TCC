# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s): 
    """função que retorna hashtag no inicio, meio e fim da string
    str -> str"""
    return '#' + s[:(len(s)//2)] + '#'