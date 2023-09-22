def qtd_divisires(num):
    """Funcao que calcula e retorna a quantidades de divisores de um determinado numero(num);
    int->int"""
    div=0
    for div in num range(1,num):
        if num%div==0:
            div=div+1
        i=i+1
        return div