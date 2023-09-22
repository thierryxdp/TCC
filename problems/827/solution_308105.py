def qtd_divisores(numero):
    ls_atual = []
    if numero>0:
        intervalo = list(range(0, numero+1))
    if numero<0:
        return 0
    list.remove(intervalo, 0)
    for i in intervalo:
        if numero%i == 0:
            list.append(ls_atual, i)
    return len(ls_atual)