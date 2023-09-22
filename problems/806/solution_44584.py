def colisao(ret1,ret2):
    '''Retorna  true quando há colisão entre dois objetos dadas as coordenadas de cada um e retorna false caso não haja colisão
Tupla,tupla -> valor booleano'''

      if ret1[0] <= ret2[2] and ret1[1] <= ret2[3]:
        return True
    else:
        return False

    if ret2[0] <= ret1[2] and ret2[1] <= ret1[3]:
        return True
    else: 
        return False

  if ret1[0] <= ret2[0] and ret1[1] <= ret2[2]:
        return True
    else:
        return False 

    if ret1[2] <= ret2[2] and ret1[3] <= ret2[3]:
        return True
    else:
        return False