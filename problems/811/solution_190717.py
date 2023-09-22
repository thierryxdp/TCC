'''Função que calcula as medidas de um colchao para ver se o mesmo
passa pela porta de João, tendo como parametros medidas, h=altura e l=largura
list,int,int->string'''
def colchao(medidas,H,L):
    if((medidas[1]>H and medidas[2]>H) or (medidas[0]>1)):
        return False
    else:
        return True