# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """funcao que divide a string ao meio e destaca as partes por meio de #"""
    index = len(s)//2
    string = str.partition(s,s[index])
    str(string.replace(string, ",","#"))
    return string