def qtd_divisores(n):
    """ Retorna o número de divisores de n; int -> int"""
    lista_divisores=[]
    for i in range(1,n+1):
        if n%i==0:
            list.append(lista_divisores,i);
    return len(lista_divisores);