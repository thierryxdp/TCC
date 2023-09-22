# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
import math
def hashtag(s):
    "A função insere a # no incio, meio e fim da str; str ==> str"
    meio = math.floor((len(s)/2)+1)
    s = list(s)
    s.insert(0,"#")
    s.insert(meio,"#")
    s.append("#")
    Final = "".join(s)
    return Final