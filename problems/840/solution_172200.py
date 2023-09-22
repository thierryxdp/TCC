import math

def bolos (farinha_de_trigoA, ovosB, colheres_sopa_de_leiteC):
    farinha = math.floor((farinha_de_trigoA/2))
    ovos = math.floor((ovosB/3))
    colhersop = math.floor((colheres_sopa_de_leiteC/5))

    if farinha < ovos or colhersop:
     return math.floor(farinha/2)
    else:
        if ovos < colhersop or farinha:
         return mayh.floor(ovos/3)
        else:
            if colhersop < ovos or farinha:
             return math.floor(colhersop/5)
            else:
                return farinha