# funcao que recebe uma string e insere o caractere '#' no inicio, meio e final dela
# str-> str
def hashtag(s):
    import math
    meio = len(s)/2
    meio = math.floor(meio)
    p1 = s[0:meio]
    p2 = s[meio:]
    return '#'+p1+'#'+p2+'#'