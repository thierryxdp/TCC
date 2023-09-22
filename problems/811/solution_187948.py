# Função que retorna se as medidas da porta batem com as do colchão
# Escolha nomes elucidativos para suas variáveis
# lista,int,int -> bool
def colchao(medidas,H,L):
    medidas = [A,B,C]
    if H > A and B:
        return 'False'
    elif H > A and C:
        return 'False'
    elif H > B and C:
        return 'False'
    elif L > A and B:
        return 'False'
    elif L > A and C:
        return 'False'
    elif L > B and C:
        return 'False'
    else:
        return'True'