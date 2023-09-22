# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Função em que dada uma string s retorna ela com hashtags (#) no início, meio e fim da string.
    string -> string"""
    import math
    from math import floor
    vol = math.floor(len(s)/2)
    ini = s[0:vol]
    fim = s[vol:]
    return str('#') + ini + str('#') + fim + str('#')