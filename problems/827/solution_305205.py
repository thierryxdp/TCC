def qtd_divisires(num):
    """Funcao que calcula e retorna a quantidades de divisores de um determinado numero(num);
    int->int"""
    soma=''
    i=0
    for i in num:
        if (num%i)==0:
            soma=soma+num
    return soma