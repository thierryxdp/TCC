def colchao(A,B,C,H,L);
'''Função que dado uma lista com as dimensoes do colchao,a altura e a largura da porta,retora se o colchao passa pela porta ou nao.
list,int,int->bool'''
if B<H and A<L:
    return True
else:
    return False