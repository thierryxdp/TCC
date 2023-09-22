def colchao (medidas,h,l):
    '''funcao que recebe as dimensoes de colchao (medidas), e as medidas das portas da sua casa em altura (h) e largura (l), todas em centímetros. E QUE RETORNA SE O COLCHAO COM AS MEDIDAS ENVIADAS VAO PASSAR ATRAVES DA PORTA DA CASA;
    lista, int, int -> bool '''
    altura_colchao = medidas[0]
    comprimento_colchao = medidas[1]
    largura_colchao = medidas[2]
    
    if (comprimento_colchao>altura_colchao):
        if (largura_colchao>1):
            return False
        elif (largura_colchao<1):
            return True
    else:
            return True