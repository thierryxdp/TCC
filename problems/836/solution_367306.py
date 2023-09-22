def busca(a,b):
    """faz uma busca por funcionarios em um determinado setor;
    list, string -> list"""
    lis = []
    for x in range(len(a)):
        if b in a[x][3]:
            lis = lis + a[x]
    return lis