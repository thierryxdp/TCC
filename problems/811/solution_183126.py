# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchão(medidas,H,L):
    '''Função que define se o colchão que joão pretende comprar irá passar pelas portas de sua casa. Essa função usa uma lista [A,B,C] como parâmetro, onde A é a espessura do colchão, B é a largura e C a altura. Outros parametros, que são H(altura da porta) e L(largura da porta); list,int,int-bolean'''
    if H>=medidas[1] or H>=medidas[2] or L>=medidas[1]:
        return True
    else:
        return False