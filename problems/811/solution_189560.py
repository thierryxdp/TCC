# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medida,h,l):
	'''Determina se um objeto passa por uma porta com dimensões h e l dados altura largua e comprimento(medida[]) 
    lista, int, int --> bool'''
    if(medida[0] <= l) and (medida[1] <= h):
        return True
    elif(medida[0] <= h) and (medida[1] <= l):
         return True
    else: 
         return False