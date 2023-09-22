def colchao(medidas,H,L):
    """retorna se é possível passar um colchão por uma 
    porta dados as medidas do colchão e as medidas da porta 
    em centímetros
    list, int, int -> bool"""
    h_colchao=medidas[0]
    l_colchao=medidas[1]
    c_colchao=medidas[2]
    
    return int(c_colchao)>H and int(l_colchao)>H not (int(c_colchao)<L or int(l_colchao)<L)
       
    
    
    # Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis