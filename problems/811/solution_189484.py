def colchao(medidas,H,L):
    """retorna se é possível passar um colchão por uma 
    porta dados as medidas do colchão e as medidas da porta 
    em centímetros
    list, int, int -> bool"""
    h_colchao=medidas[0]
    l_colchao=medidas[1]
    c_colchao=medidas[2]
    if int(c_colchao)>H and int(l_colchao)>H or int(h_colchao)>L:
        return False
    else:
        return True
    
    
    
    # Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis