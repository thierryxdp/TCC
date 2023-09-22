def qtd_divisores(num):
    '''
        funcao que conta quantos divisores um dado numero inteiro tem.
        lista:list
        num:int
        return:int
    '''
    lista = []
    for i in range(1, num + 1):
        if num % i == 0:
            lista.append(i)
    return len(lista)