def qtd_divisores(i):
    l = []
    for n in range(1, i):
        if i % n == 0:
            list.append(l, n)
        if i not in l:
            list.append(l, i)
    return len(l)
def primo(i):
    if qtd_divisores(i) == 2:
        return True
    else:
        return False