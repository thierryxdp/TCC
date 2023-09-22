def eh_quadrada(M):
    """coment"""
    linhas=len(M)
    for linha in M:
        if len(linha)!=linhas:
            return False
    return True