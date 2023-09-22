def qtd_divisores(num):
    """Funcao que calcula e retorna a quantidades de divisores de um determinado numero(num);
    int->int"""
    div=[]
    for n in range(1,num+1):
        if num%n==0:
            div.append(n)
    return len(div)