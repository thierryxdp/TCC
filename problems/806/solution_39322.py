#Start your python function here
def colisao(ret1,ret2):
    "dadas duas tuplas formadas pelas coordenadas de um retangunlo, retorna True caso haja interseção entre eles e false caso não haja. tupla (int, int), tupla(int, int) -> bool"
    if ret1[2] < ret2[0]:
        return False
    elif ret1[0] > ret2[2]:
        return False
    elif ret1[1] > ret2[3]:
        return False
    if ret1[3] < ret2[1]:
        return False
    else:
        return True