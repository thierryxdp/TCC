# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Retorne o caractere '#' no início, meio e no final de uma string s"""
    s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#" 
    return s