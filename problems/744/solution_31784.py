# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Função que retorna o caracter # no começo,meio e final da string"""
    meio=len(s)//2
    return "#"+s[:meio]+"#"+s[meio:]