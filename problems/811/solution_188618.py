# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def passar_colchao([a,b,c],h,l)
#variáveis do colchão
a,b
#variáveis da porta
h,l

altura_do_colchao = a
largura_do_colchao = b
altura_da_porta = h
largura_da_porta = l

if (altura_do_colchao <= altura_da_porta) and (largura_do_colchao <= largura_da_porta):
    return True
else:
    return False