def qtd_divisores(numero):
    'Função que recebe um número e indica a quantidade de divisores dele.'
    'int->int'
    lista=[]
    for divisor in range(1,numero+1):
        if numero%divisor==0:
            lista=lista+[divisor]
    return len(lista)