def colchao(medidas,H,L):
    '''funcao que diz se um colchao passa ou nao da porta de joao dados as as medidas do 
    colchao em medidas, altura da porta em H e largura da porta em L
    lista de int,int,int -->bool'''
    return medidas[1]<=H and medidas[0]<=L  or medidas[0]<=H and medidas[1]<=L