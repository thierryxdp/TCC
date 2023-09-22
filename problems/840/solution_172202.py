import math

def bolos (farinha_de_trigoA, ovosB, colheres_sopa_de_leiteC):
    farinha = math.floor((farinha_de_trigoA/2))
    ovos = math.floor((ovosB/3))
    colhersop = math.floor((colheres_sopa_de_leiteC/5))

    if farinha < ovos or colhersop not == 0:
     return farinha
    else:
        if ovos < colhersop or farinha not == 0:
         return ovos
        else:
            if colhersop < ovos or farinha not == 0:
             return colhersop