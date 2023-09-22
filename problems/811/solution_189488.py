def colchao(medidas,H,L):
    """retorna se é possível passar um colchão por uma 
    porta dados as medidas do colchão e as medidas da porta 
    em centímetros
    list, int, int -> bool"""
    h_colchao=int(medidas[0])
    l_colchao=int(medidas[1])
    c_colchao=int(medidas[2])
    if c_colchao>H and l_colchao>H and c_colchao>L and l_colchao>L:
        return False
    else:
        return True
    
       
    
    
    # Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis