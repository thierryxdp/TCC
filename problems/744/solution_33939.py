# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
import math
def hashtag(s):
    "Retorna a string s com hashtags no início, meio e final."
    metade = math.floor(len(s)/2)
    return "#"+s[:metade]+"#"+[metade:]+"#"