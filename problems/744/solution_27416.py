# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """ essa função irá colocar uma hashtag "#"no inicio, no meio e no final de cada string s
    str -> str """
    v = len(s)//2
    return "#" + s[0:v]+ "#" + s[v:] + "#"