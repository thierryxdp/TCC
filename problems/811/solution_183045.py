def colchao(medidas,H,L);
'''Função que dado uma lista com as dimensoes do colchao,a altura e a largura da porta,retora se o colchao passa pela porta ou nao.
list,int,int->bool'''
if L>=medias[0] and H>=medidas[1]:
    return True
else:
    return False