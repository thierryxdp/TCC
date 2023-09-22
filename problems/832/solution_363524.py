def eh_quadrada(M):
    """Função que identifica se a matriz é quadrada ou não;
    list(list) -> bool"""
    
    linhas = len(M)
    colunas = len(M[0])
    
    if linhas > colunas or linhas < colunas:
        return "False"
    else:
        return "True"