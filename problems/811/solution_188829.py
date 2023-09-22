# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    '''todas as entradas sao inteiros medidos em cm'''
    #h é altura da porta
    # l largura da porta
    
    A= medidas[0]
    B=medidas[1]
    C=medidas[2]
    x = min( A ,min(B,C))
    y = min( max(A,B), max(B,C) , max (A,C) )
    if H<L:
        S=L
        V=H
    
    if x<=H and x<=L:
        return True
    
    elif x<S and y<V:
        return True
    else:
        return False