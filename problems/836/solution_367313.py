def busca(a,b):
    """faz uma busca por funcionarios em um determinado setor;
    list, string -> list"""
    lis = []
    for x in range(len(b)):
        if a in b[x]:
            lis = lis + [[b[x][0]]+ [b[x][1]] + [b[x][3]]]
    return lis