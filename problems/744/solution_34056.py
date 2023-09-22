# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(string):
    meio = len(string) //2
    s= '#' + string[0:meio]+'#'+string[meio:]+'#' # meio p final.
    return s