# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
import math
def hashtag(s):
    "A função insere a # no incio, meio e fim da str; str ==> str"
    meio = int(len(s)/2)
    s = list(s)
    print(s)
    s.insert(0,"#")
    print (s)
    s.insert(meio,"#")
    print (s)
    s.append("#")
    print (s)
    Final = "".join(s)
    return Final