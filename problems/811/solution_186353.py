# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis

def colchao(medidas, H, L):
    ''' Retorna se o colchão pode passar pela porta
    	lista, int, int -> bool
        Explicação: separa os valores da lista e compara eles com H e L para saber se de alguma forma o colchão passa, retornando
        verdadeiro, caso contrário retorna falso'''
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    
    if A <= H and (B <= L or C <= L):
        return True
    if A <= L and (B <= H or C <= H):
        return True
    if B <= L and C <= H:
        return True
    if B <= H and C <= L:
        return True
    return False