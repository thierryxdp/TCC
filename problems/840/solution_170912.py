def bolos(farinha=2,ovos=3,leite=5):
    if farinha < 2:
        return int(0)
    elif ovos < 3:
        return int(0)
    elif leite < 5:
        return int(0)
    else:
    
# descobrir quantos bolos cada ingrediente pode fazer
    q_farinha = farinha/2
     q_ovos    = ovos/3
     q_leite    = leite/5

# pegar o valor mínimo entre eles
     return quantidade = min(q_farinha, q_ovos, q_leite)
   return quantidade