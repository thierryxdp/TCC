def qtd_divisores(n):
    final=0
    for i in range(n):
        if n/i==0:
            final=final+1
    return final