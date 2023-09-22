def qtd_divisores(num):
    """doc"""
    div = []
    for i in range(1,num+1):
        if (num%i) == 0:
            div.append(i)
    return len(div)