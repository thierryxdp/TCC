#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior direito do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    p_inf_retc1 = ret1[:2]
    p_sup_retc1 = ret1[2:]
    p_inf_retc2 = ret2[:2]
    p_sup_retc2 = ret2[2:]

    x,y = 0,1
    
    if (p_inf_retc1[x] <= p_inf_retc2[x] <= p_sup_retc1[x] or 
        p_inf_retc1[x] <= p_sup_retc2[x] <= p_sup_retc1[x]) and (p_inf_retc1[y] <= p_inf_retc2[y] <= p_sup_retc1[y] or 
     p_inf_retc1[y] <= p_sup_retc2[y] <= p_sup_retc1[y]):
        return True
    elif (p_inf_retc2[x] <= p_inf_retc1[x] <= p_sup_retc2[x] or 
        p_inf_retc2[x] <= p_sup_retc1[x] <= p_sup_retc2[x]) and (p_inf_retc2[y] <= p_inf_retc1[y] <= p_sup_retc2[y] or 
     p_inf_retc2[y] <= p_sup_retc1[y] <= p_sup_retc[2y]):
        return True
    return False

    return False