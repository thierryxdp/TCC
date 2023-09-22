# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """A função coloca uma hastag no começo, fim e meio de uma string"""
    return "#"+s[:len(s)//2]+"#"+s[len(s)//2:]