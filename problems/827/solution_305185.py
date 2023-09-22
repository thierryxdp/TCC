def qtd_divisires(num):
    """Funcao que calcula e retorna a quantidades de divisores de um determinado numero(num);
    int->int"""
    div=0
    i=0
    for div in range(2,num):
        if num%div==0:
            i=i+div
    return i