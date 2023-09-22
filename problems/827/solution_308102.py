def qtd_divisores(numero):
    ls_atual = []
    intervalo = range(-numero, numero+1)
    list.remove(intervalo, 0)
    for i in intervalo:
        if numero%i == 0:
            list.append(ls_atual, i)
    return len(ls_atual)