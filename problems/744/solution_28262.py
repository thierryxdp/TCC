# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
import math
def hashtag(s):
    c=len(s)
    metade=math.floor(c/2)
    return "#"+s[0:metade]+"#"+s[metade:c]+"#"