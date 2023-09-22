# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(x):
    q = len(x)//2
    return "#"+x[:q]+"#"+x[q:]+"#"