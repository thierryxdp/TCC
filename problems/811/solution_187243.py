def colchao(medidas,H,L):
    '''Função que retorna se é possível passar um colchão pela porta da casa do
    comprador. Os parâmetros as medidas de largura, comprimento e altura do retângulo,
    respectivamente e as medidas de altura e largura da porta. Lista--> boolean'''
    lagura= medidas[0]
    comprimento= medidas[1]
    altura= medidas[2]
    #com a face da altura paralela ao chão
    if((comprimento<=H or comprimento<=L)):
        return True
    elif(altura<=H or altura<=L): #com a face do comprimento X largura paralela
        return True
    else:
        return False