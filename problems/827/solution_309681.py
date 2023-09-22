def qtd_divisores(número):
    'Função que recebe um número e indica a quantidade de divisores dele.'
    'int->int'
    lista=[]
    for divisor in range(1,número+1):
        if número%divisor==0:
            lista=lista+[divisor]
    return len(lista)