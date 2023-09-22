def colchao(medidas, H,L):

    A = medidas[0]   
    B = medidas[1]
    C = medidas[2]

    if (H >= B and L >= A):    #verificação passagem longitudinal do colchão
        return True
    elif (L >= B and H >= A):  #verificação passagem transversal do colchão
        return True
    elif (H >= C and L >= A):  #verificação passagem com a maior dimensão paralela à altura da porta
        return True
    else:
        return False