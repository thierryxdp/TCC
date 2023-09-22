#Start your python function here
def pontost1(jogo):
    pontos=jogo[0][2][0] + jogo[1][2][0]
    return pontos
def pontost2(jogo):
    pontos=jogo[0][2][1] + jogo[1][2][1]
    return pontos
def pontos_por_time(jogo):
    return {jogo[0][0]:pontost1(jogo),jogo[0][1]:pontost2(jogo)}