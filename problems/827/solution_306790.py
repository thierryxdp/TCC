def qtd_divisores(numero):
    """função que retorna a quantidade de divisores de um numero
    int -> int"""
    lista=[]
    for n in range(1,numero+1):
        if (numero%n)==0:
            lista.append(n)
    return len(lista)