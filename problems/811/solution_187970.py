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
    medidas[0] = esp
    medidas[1] = larg
    medidas[2] = alt
    
    if (esp<L and larg<H)or(esp<L and alt<H)or(larg<L and esp<H)or(larg<L and alt<H):
        return True
    else:
        return False