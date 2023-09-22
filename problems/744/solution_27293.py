# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Nessa função será adicionado "#" no inicio, meio e fim da
    string. 
    str -> str"""
    string = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return string