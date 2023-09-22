# Função que retorna se as medidas da porta batem com as do colchão
# Escolha nomes elucidativos para suas variáveis
# lista,int,int -> bool
def colchao(medidas,H,L):
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    if A and B <= H or L:
        return True
    elif A and C <= H or L:
        return True
    elif B and C <= H or L:
        return True
    else:
        return False