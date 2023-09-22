# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
import math
def hashtag(s):
    string_size = len(s)
    import math
    if(string_size % 2 == 0):
        return "#"+s[0: math.floor(string_size/2)]+"#" + s[math.floor(string_size/2):]+"#"
    else:
        return "#" + s[0: math.floor(string_size / 2)] + "#" + s[int(math.floor(string_size / 2)+0.5):] + "#"] + "#"