def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro 
    valores inteiros cada um, representando as coordenadas 
    dos vertices inferior esquerdo e superior direito do 
    primeiro e do segundo retângulo nessa ordem. Devolve
    True se ha colisao entre os 2 retangulos ou False, caso 
    contrario. 
     (tuple),(tuple) --> bool'''
    if ret1[0] == ret2[0] and ret1[1] == ret2[1]:
        return True
    elif ret1[2] == ret2[2] and ret1[3] == ret2[3]:
        return True
    elif ret1[0] == ret2[0] and ((ret1[1] >= ret2[1] and ret1[3] >= ret2[3]) or (ret1[2] >= ret2[2] and ret1[3] <= ret2[3])):
        return True
    elif ret1[0] <= ret2[0] and ret1[1] >= ret2[1] and ret1[2] <= ret2[2] and ret1[3] <= ret2[3]:
        return True
    else:
        return False