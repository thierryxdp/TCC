def qtd_divisores(numero):
    ls_atual = []
    divisores = (1,2,3,4,5,6,7,8,9,10)
    for i in divisores:
        if numero%i == 0:
            list.append(ls_atual, i)
    return len(ls_atual)