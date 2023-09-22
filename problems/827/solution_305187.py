def qtd_divisires(num):
    """Funcao que calcula e retorna a quantidades de divisores de um determinado numero(num);
    int->int"""
    soma=0
    i=0
    for i in range(2,num):
        if num%i==0:
            soma=soma+num
    return soma