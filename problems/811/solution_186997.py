#Colchão:
''' Essa função confere se um colchão passa ou não por determinada porta. '''
''' list, int ---> bool. '''

def colchao(medidas, H, L):
    
    #definindo a altura, largura e comprimento da porta em cm:
    altura_colchão = medidas[1]
    largura_colchão = medidas[0]
    comprimento_colchão = medidas[2]
    
    #definindo as condições para "True" e "False":
    if  altura_colchão<=H and largura_colchão<=L:
        return True
    else:
        return False