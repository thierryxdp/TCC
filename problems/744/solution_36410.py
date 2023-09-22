# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
import math
def hashtag(s):
    "A função insere a # no incio, meio e fim da str; str ==> str"
    meio = math.floor(len(s)/2)
    s = list(s)
    print(s)
    s = s.insert(0,"#")
    s = s.insert(meio,"#")
    s = s.append("#")
    s = "".join(s)
    return s