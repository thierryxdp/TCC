def qtd_divisires(num):
    """Funcao que calcula e retorna a quantidades de divisores de um determinado numero(num);
    int->int"""
    div=0
    i=0
    for div in range(1,num):
        if num%div==0:
            div=div+1
    if div==0:
        return 1
    else:
        return 0
    return div