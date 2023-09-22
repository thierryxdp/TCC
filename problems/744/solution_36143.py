# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(str1):
    "coloca hashtags no começo, no meio e no final da string que for inserida str->str"
    str1= '#'+ str1[:len(str1)//2]+'#'+ str1[len(str1)//2]+'#'
    return str1