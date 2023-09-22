# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
   tam = len(s)
    return "#" + s[:tam/2] + "#" + s[tam//2:]+"#"