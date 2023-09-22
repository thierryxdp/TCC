def qtd_divisores(n):
    """ A função retorna a quantidade de divisores positivos inteiros de um número inteiro n;
    int -> int """
    ls=[]
    i=1
    for i in range(1,n+1):
        if n%i == 0:
            ls.append(i)
        i+=1
    return len(ls)