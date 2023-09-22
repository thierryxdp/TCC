# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    strg1=  "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#" 
    return strg1