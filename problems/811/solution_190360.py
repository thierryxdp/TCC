# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medida,H,L):
	'''Função que determina se um colchão passa (True), ou não (False), por uma porta com dimensões H e L, altura e largua respectivamente. 
    list, int, int --> bool'''
    if(medida[0] <= L) and (medida[1] <= H):
        return True
    elif(medida[0] <= H) and (medida[2] <= L):
         return True
    else: 
         return False