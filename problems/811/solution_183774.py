# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """A função verifica se um colchão com dimensões A,B,C passa por uma porta de altura H e largura L
    As dimensões devem ser colocadas no parâmetro medida da menor para a maior
    lista,int->bool"""
    return medidas[1]<=H and medidas[0]<=L or (medidas[1]<=L and medidas[0]<=H)