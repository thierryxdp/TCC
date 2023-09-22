def hashtag(s):
    """Calcula e retorna a inserção do caractere "#" no inicio, no meio e no fim de uma string
    Entradas: string(s)
    string-->string"""
    primeira_particao = str(s[0:len(s)//2])
    segunda_particao = str(s[len(s)//2:])
    return '#'+str(primeira_particao)+'#'+str(segunda_particao)+'#'