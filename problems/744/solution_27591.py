# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''A função recebe uma string e insere "#" no começo, meio e final da string.
       Parametros: str -> str'''
    antes = s[:len(s)//2]
    depois = s[len(s)//2:]
    return "#" + antes + "#" + depois + "#"