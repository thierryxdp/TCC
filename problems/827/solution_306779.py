def qtd_divisores(numero):
    """ Retorna quantos divisores um número tem;
    int -> int"""
    listanum = list(range(1, numero+1))
    i = 0
    div = [n for n in listanum if numero%n==0]
    return len(div)