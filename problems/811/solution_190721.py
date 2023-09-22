'''Função que calcula as medidas de um colchao para ver se o mesmo
passa pela porta de João, tendo como parametros medidas que é uma lista
com as dimensoes do colchao em centimetros, ordenadas da
menor para a maior, h=altura e l=largura.
list,int,int->string'''
def colchao(medidas,H,L):
    if(medidas[1]<H and medidas[2]<H):
        return True
    elif(medidas[1]<1 and medidas[2]<1):
        return True
    else:
        return True