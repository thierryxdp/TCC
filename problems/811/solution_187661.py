def colchao(medidas,H,L):
    '''Função que calcula se joão consegue ou não passar 
    com o colchão pela porta de sua casa, com variaveis como 
    H= altura da porta L= largura da porta e medidas como
    as medidas do colchão
    entrada=list,int,int
    saida=bool'''
    x=medidas[1]
    y=medidas[2]
    if (x>H and y>H) and (x>L and y>L):
        return False
    else:
        return True