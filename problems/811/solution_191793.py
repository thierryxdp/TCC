# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    '''Dadas a medida em uma lista com numeros inteiros e a altura (H)
    e largura da porta (L), que responde se o colchao pode passar pela porta.
    int,int,int->bool'''
    
    
    if min(medidas[1],medidas[2])<=H :
        return True
    if min(medidas[1],medidas[2])<=L:
        return True
    else:
        return False