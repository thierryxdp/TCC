# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Retorna uma string com "#" inserida em seu inicio, meio e final
    str -> str"""
    x=len(s)
    y=x//2
    return "#"+s[:y]+"#"+s[y:]+"#"