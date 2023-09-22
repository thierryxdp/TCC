def qtd_divisores(numero):
    ls_atual = []
    for i in range(-numero,numero+1):
        if numero%i == 0:
            list.append(ls_atual, i)
    return len(ls_atual)