# str-> str
def hashtag(s):
    #depara s em duas partes, e acrescenta # antes, entre e depois. Len(s) pra pegar a quantidade de caracteres e //2 para retornar a parte inteira da divisao
    return'#'+s[0:len(s)//2]+'#'+s[len(s)//2:]+'#'