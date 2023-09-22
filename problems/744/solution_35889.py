# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    y = (len(s))/2
    a = s[0:y-1]
    b = s[-1:-y:-1]
    return f"# {a} # {b} #"