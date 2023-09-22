import math

def bolos (farinha_de_trigoA, ovosB, colheres_sopa_de_leiteC):
    farinha = math.floor((farinha_de_trigoA/2))
    ovos = math.floor((ovosB/3))
    colhersop = math.floor((colheres_sopa_de_leiteC/5))

    if farinha < ovos and colhersop or farinha == 0:
     return farinha
    else:
        if ovos < colhersop and farinha or ovos == 0:
         return ovos
        else:
            if colhersop < ovos and farinha or colhersop == 0:
             return colhersop