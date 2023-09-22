# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """coloque uam "#" no começo, meio e fim de uma string."""
    i=len(s)//2
    return "#"+s[0:i]+"#"+s[i:]+"#"