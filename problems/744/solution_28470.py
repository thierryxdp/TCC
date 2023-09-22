# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(string):
    "Função que retorna a string inserida com # no inicio, meio e final dela. str -> str"
    x = len(string)//2
    return "#" + string[:x] + "#" + string[x:] + "#"