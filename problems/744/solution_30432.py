# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    "função que insere um hashtag no começo, no meio e no final de uma string"
    "str -> str"
    return "#"+(s[0:len(s)//2])+"#"+(s[len(s)//2:])+"#"