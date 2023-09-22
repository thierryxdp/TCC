def qtd_divisores(numero):
    lista=[]
    for n in range(1,numero+1):
        if (numero%n)==0:
            lista.append(n)
    return len(lista)