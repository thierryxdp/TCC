# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Funcao que dada uma string retorna ela com # no seu
    inicio, meio e fim
    str-->str"""
    x = len(s)
    y = x//2 
    nova_str = "#" + s[0:y] + "#" + s[y:] + "#"
    return nova_str