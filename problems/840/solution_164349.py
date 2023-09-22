'''A receita:
	A- 2 xícaras de farinha
    B- 3 ovos
    C- 5 colheres de sopa de leite
'''

def bolos(A, B, C):
    '''A quantidade de bolos que ele pode fazer vai ser determinada
    pela quantidade de bolos que ele consegue fazer com o ingrediente limitante.
    Nesse caso, o ingrediente limitante vai ser aquele com o menor resultado da 
    divisão 
    	Quantidade deste ingrediente disponivel / Quantidade necessária
    
    Como João não se garante na cozinha, ele somente vai fazer números inteiros de bolos'''
    qnt_pela_xicara = A // 2
    qnt_pelo_ovo = B // 3
    qnt_pela_sopa = C // 5
    
    quantidade = min(qnt_pela_xicara, qnt_pelo_ovo, qnt_pela_sopa)
    return quantidade