def qtd_divisores(numero):
    listanum = list(range(1, numero+1))
    i = 0
    div = [n for n in listanum if numero%n==0]
    return div