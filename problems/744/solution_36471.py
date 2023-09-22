# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    return "#"+es(s)+"#"+dr(s)+"#"
def es(x):
    return x[:len(x)//2]
def dr(x):
    return x[len(x)//2:]