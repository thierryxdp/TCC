# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """função que adiciona uma # no início meio e fim da string; str -> str"""
    t=len(s)
    p=int(t/2)
    return "#"+s[0:p]+"#"+s[:p]+"#"