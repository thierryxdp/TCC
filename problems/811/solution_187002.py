#Colchão:
''' Essa função confere se um colchão passa ou não por determinada porta. '''
''' list, int ---> bool. '''

def colchao(medidas, H, L):
    
    #definindo a altura, largura e comprimento da porta em cm:
    altura_colchao = medidas[1]
    largura_colchao = medidas[0]
    comprimento_colchao = medidas[2]
    
    #definindo as condições para "True" e "False":
    if  altura_colchao<=H or largura_colchao<=L:
        return True
    else:
        return False