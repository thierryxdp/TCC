def qtd_divisores(numero):
    listanum = list(range(1, numero+1))
    i = 0
    div = [n for n in listanum if n%2==0]
    return div