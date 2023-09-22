def eh_quadrada(M):
    """Função que identifica se a matriz é quadrada ou não;
    list(list) -> bool"""
    
    linhas = len(M)
    colunas = len(M[0])
    
    if colunas == linhas:
        return "True"
    if len(M) == 0:
        return "True"
    else:
        return "False"