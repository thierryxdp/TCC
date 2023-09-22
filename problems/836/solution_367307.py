def busca(a,b):
    """faz uma busca por funcionarios em um determinado setor;
    list, string -> list"""
    lis = []
    for x in range(len(b)):
        if a in b[x][3]:
            lis = lis + b[x]
    return lis