def qtd_divisores(num):

quantidade = filter(lambda x: num%x == 0,range(1, num+1))
quatidade = list(quantidade)

    return len(quantidade)