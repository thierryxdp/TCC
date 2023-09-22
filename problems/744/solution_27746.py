# Função que recebe uma string e retorna a mesma com o caractere '#'
# no inicio, meio e fim da string
# str-> str
def hashtag(s):
    meio= len(s)//2
    return '#'+s[:meio]+'#'+s[meio:]+'#'