def eh_quadrada(M):
    """Dado como entrada uma matriz, retorna se a matriz é quadrada ou 
    não a partir de um booleano;
    list(list)->bool"""
    linhas=len(M)
    for linha in M:
        if len(linha)!=linhas:
            return False
    return True