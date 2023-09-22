# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """recebe uma string e insere o caractere '#' no inicio, meio e fim dela
       str->str"""
    s="#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"