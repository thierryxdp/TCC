def n_bolos(A,B,C):
    """função que calcula o número máximo de bolos que é possivel fazer com as quantidades 'A','B' e 'C' de ingredientes disponíveis em relação as quantidades proporcionais para cada entrada 
    
    as quantidades mínimas para cada ingrediente são respectivamente: A-2 (xícaras de farinha de trigo); B-3 (ovos); C-5 (colheres de sopa de leite) """
    return int(min(A/2,B/3,C/5))