# Função que retorna se as medidas da porta batem com as do colchão
# Escolha nomes elucidativos para suas variáveis
# lista,int,int -> bool
def colchao(medidas,H,L):
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    if H or L >= A and B:
        return True
    elif H or L >= A and C:
        return True
    elif H or L >= B and C:
        return True
    else:
        return False