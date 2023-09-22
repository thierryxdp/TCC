def qtd_divisores(num):
    """funcao que retorna a quantidade de divisores de um numero
dado
int->int"""
    qtd = []
    for x in range(1,num + 1):
        if num%x == 0:
            list.append(qtd,x)
    return len(qtd)