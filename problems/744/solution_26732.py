def hashtag(s):
#Função que adiciona # no inicio, meio e fim de uma string dada como entrada.
#Entrada: string.
#Saida: string.
    return '#'+s[0:(len(s)//2)]+'#'+s[(len(s)//2):]+'#'