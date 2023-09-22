def colchao(medidas, H,L):
    """função que recebe uma lista de tamanho 3, contendo as medidas do colchão em cm,ordenada do maior para o menor e H sendo a altura da porta e L aa largura da mesma. A função retorna True se o colchão passar pela porta e false, caso contrário. 
    list,int,int->bool"""
    if (medidas[1] <= H) or (medidas [2]<= L):
        return True
    else:
        return False