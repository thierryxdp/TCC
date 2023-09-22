def colchao(medidas,H,L):
    'Dadas, respectivamente, as medidas (dimensoes) de um colchao, de forma crescente, a altura H e  largura L das portas de uma casa, a funcao retorna True se o colchao passaria pela porta e False caso contrario. List, int, int -> Bool'
    if medidas[1]<= H or medidas[1]<= L and medidas[0]<= L:
        return True
    else:
        return False