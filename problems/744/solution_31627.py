# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Colocar hashtags no início, meio e fim da string"""
    meio=int(len(s)/2)
    return "#"+s[:meio]+"#"+s[(meio):]+"#"