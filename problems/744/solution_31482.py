# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    X=s
    t=len(X)
    return "#"+X[0:(t//2)]+"#"+X[(t//2):]+"#"