# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    '''
    	Funcao recebe uma lista(medidas) com as medidas, em
        centimetros, do colchao ordenadas da menor pra maior,
        a altura(H) e a largura(L) da porta, ambas em centimetros,
        e retorna True se o colchao passa pela porta e False, 
        caso contrario
        list, float, float -> bool
        
    '''
    if (medidas[0]<=L and medidas[1]<=H) or (medidas[0]<=L and medidas[2]<=H) or (medidas[0]<=L and medidas[2]<=L):
        return True
    else:
        return False