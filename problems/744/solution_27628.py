# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
#Recebe uma string(s) e a retorna com adição de "#" no início, meio e final da string
#str -> str
    x = str("#")
    return x + s[:len(s)//2] + x + s[len(s)//2:] + x