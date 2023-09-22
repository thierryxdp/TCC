def qtd_divisores (numero):
    '''calcula e retorna a quantidade de divisores que o número tem'''
    '''int->int'''
    div= []
    for i in range(1,numero+1):
        if numero%i == 0:
            list.append (div,i)
    return len(div)