# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    '''A partir das medidas do colchão recebida como uma lista e das medidas da porta respectivamente altura e largura;
    retorna a possibilidade de passar ou não pela porta com o colchao;
    list, int, int => bool'''
    A,B,C = medidas
    
    if (int(B)<=H and int(A)<=L) or (int(C)<=H and int(A)<=L):
        return True
    else:
        return False