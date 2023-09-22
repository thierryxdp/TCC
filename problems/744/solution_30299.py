# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    "retorna uma string com '#' no inicio, meio e fim"
    #pre = s[:len(s)//2]
    #pos = s[len(s)//2:]
    #s = "#" + pre + "#" + pos + "#"
    s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return s