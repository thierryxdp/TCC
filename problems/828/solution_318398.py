def qtd_divisores(num):
    """doc"""
    div = []
    for i in range(1,num+1):
        if (num%i) == 0:
            div.append(i)
    return len(div)

def primo(num):
    """doc"""
    if qtd_divisores(num) != 2:
        return False
    return True