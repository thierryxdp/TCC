# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """insere '#' no inicio, meio e final da string"""
    meio=len(s)//2
    return "#"+s[:meio]+"#"+s[meio:]+"#"