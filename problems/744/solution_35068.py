# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    "Insere o caractere # no inicio, meio e final de uma string"
    h1 = s[0:len(s)//2]
    h2 = s[len(s)//2:len(s)]
    return "#" + h1 + "#" + h2 + "#"