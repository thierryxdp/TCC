def maiores(lista_numero,n):
    '''dadaos uma lista de numeros inteiros compara com outro numero
    inteiro e retorna os valores maiores que este numero'''
    '''list,int->list'''
    new=[]
    start=0
    while start < len(lista_numero):
        if lista_numero[start] > n:
            new = new + [lista_numero[start],]
        start = start + 1
    list.sort(new)
    return new