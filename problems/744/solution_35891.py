# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Coloca # no início, meio e fim da função"""
    y = (len(s))/2
    a = hashtag[0:y-1]
    b = hashtag[-1:-y:-1]
    return f"# {a} # {b} #"