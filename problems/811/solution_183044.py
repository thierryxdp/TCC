def colchao(medidas,H,L);
'''Função que dado uma lista com as dimensoes do colchao,a altura e a largura da porta,retora se o colchao passa pela porta ou nao.
list,int,int->bool'''
if medidas[1]>H and medidas[0]>L:
    return True
else:
    return False