def eh_quadrada(m:list) -> bool:
    """função que retorna uma boleana caso a matriz dada como parâmetro seja quadrada ou não.
    
    parâmetros:
    list -> bool
    
    exemplos:
    eh_quadrada([[1,1],[1,1]])==True
    eh_quadrada([[1,1,2],[1,1,2]])==False
    eh_quadrada([])==True"""
    return len(m)==0 or len(m)==len(m[0])