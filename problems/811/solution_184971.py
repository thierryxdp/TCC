# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
    '''Função que dados uma lista de medidas do colchão em numeros inteiros, e as dimensões das portas da casa, H para altura e L para largura, em numeros inteiros, retorna True para caso o colchão passe pelas portas, ou False caso não passse.
    list, int, int -> bool'''
    m1 = medidas[0]
    m2 = medidas[1]
    
    if (m2 <= H and m1 <= L) or (m2 <= L and m1 <= H):
        return True
    else:
        return False