def qtd_divisores(numero):
    tamanho= numero+1
    lista=[]
    for divisor in range(1,tamanho):
        if numero%divisor==0:
            lista.append(divisor)
    return len(lista)