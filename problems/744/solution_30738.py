# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
import math
def hashtag(s):
    x=(len(s))/2    
    z=math.floor(x)    
    return "#"+s[:z]+"#"+(s[z:])+"#"