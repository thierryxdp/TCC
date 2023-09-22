import math
def bolos(x_trigo,ovos,c_leite):#1 bolo = 2 x_trigo 3 ovos 5 c_leite
    if((math.ceil(x_trigo/2)==0)or(math.ceil(ovos/3)==0)or(math.ceil(c_leite/5)==0)):
        return 0
    else:
        return min(math.ceil(x_trigo/2),math.ceil(ovos/3),math.ceil(c_leite/5))