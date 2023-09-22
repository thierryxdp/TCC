def concatenacao(a, b):
    """Funcao que retorna a concatenação das strings fornecidas;
    str, str -> str"""
    v1 = str(a[0:-1])
    v2 = str(b[0:-1:-1])
    
    return v1+v2