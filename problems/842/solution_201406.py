def pontos_por_time(jogos):

    " inserir os times juntamente com o resultado do jogo de ida e de volta exp: ([cormengo,flamintias],[1,0],[flamintias,cormengo],[2,2]) "
    if jogos[0][2][0] > jogos[0][2][1] and jogos[1][2][0] < jogos[1][2][1]:
        return {str(jogos[0][0] ): 6, str(jogos[0][1]): 0}
    "Verifica se o time (A) ganhou os 2 jogos e adiciona 6 pontos para ele "
    if jogos[0][2][0] < jogos[0][2][1] and jogos[1][2][0] > jogos[1][2][1]:
        return {str(jogos[0][0] ): 0, str(jogos[0][1]): 6}
    "Verifica se o time (B) ganhou os 2 jogos e adiciona 6 pontos para ele "
    if jogos[0][2][0] > jogos[0][2][1] and jogos[1][2][0] > jogos[1][2][1] or jogos[0][2][0] < jogos[0][2][1] and jogos[1][2][0] < jogos[1][2][1]:
        return { str(jogos[0][0] ): 3, str(jogos[0][1]) : 3 }
    "Verifica se os times pelo menos ganharam 1 jogo  "
    if jogos[0][2][0] == jogos[0][2][1] and jogos[1][2][0] == jogos[1][2][1] :
        return { str(jogos[0][0] ): 2 , str(jogos[0][1]) : 2 }
    "Verifica se os times empataram os jogos "
    if jogos[0][2][0] == jogos[0][2][1] and jogos[1][2][0] < jogos[1][2][1] or jogos[0][2][0] > jogos[0][2][1] and jogos[1][2][0] == jogos[1][2][1]:
        return { str(jogos[0][0] ): 4, str(jogos[0][1]): 1}
    "Verifica se o time (A) empatou um jogo e ganhou o outro  "
    if jogos[0][2][0] == jogos[0][2][1] and jogos[1][2][0] > jogos[1][2][1] or jogos[0][2][0] < jogos[0][2][1] and jogos[1][2][0] == jogos[1][2][1]:
        return {str(jogos[0][0]): 1, str(jogos[0][1]): 4}
    "Verifica se o time (B) empatou um jogo e ganhou o outro  "