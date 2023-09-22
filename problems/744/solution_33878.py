# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """A função que incrementa '#' no início,
    no meio e no fim de uma string"""
    n= len(s)
    ind = (n//2)
    return "#"+str(s[0:ind])+"#"+str(s[ind:])+"#"