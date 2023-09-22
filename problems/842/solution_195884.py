#Start your python function here
def pontos_por_time(jogosi,jogosv):
    if jogosi(2) > jogosi(3):
        pontosCi = jogosi(0) + (int(jogosi(2))*3)
        pontosFi = jogosi(1) + (jogosi(3)*0)
    elif jogosi(2) == jogosi(3):
        pontosCi = jogosi(0) + (jogosi(2)*1)
        pontosFi = jogosi(1) + (jogosi(3)*1)
    elif jogosi(2) < jogosi(3):
        pontosCi = jogosi(0) + (jogosi(2)*0)
        pontosFi = jogosi(1) + (jogosi(3)*3)
    else:
        return 0
    
    if jogosv(2) > jogosv(3):
        pontosCv = (jogosv(2)*3)
        pontosFv = (jogosv(3)*0)
    elif jogosv(2) == jogosv(3):
        pontosCv = (jogosv(2)*1)
        pontosFv = (jogosv(3)*1)
    elif jogosv(2) < jogosv(3):
        pontosCv = (jogosv(2)*0)
        pontosFv = (jogosv(3)*3)
    else:
        return 0
return pontosCi + pontosCv,pontosFi + pontosFv