# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
    '''função que dadas as medidas A,B,C de um colchão e a largura L e altura H de uma porta, retorna
       True se o colchão passa pela porta e False caso contrário. list(int,int,int),int,int -> bool'''
    if (medidas[2] <= H) and ((medidas[1] <= L) or (medidas[0] <= L)):
        return True
    elif (medidas[2] > H) and (medidas[1] <= H) and (medidas[0] <= L):
        return True
    else:
        return False