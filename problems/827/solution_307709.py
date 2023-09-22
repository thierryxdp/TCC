def qtd_divisores(num):
    """ Dado um número qualquer retorna a quantidade de divisores desse números;
    int-> int """
    lista=[]
    if num<0:
        return 0
    for i in list(range(1,num)):
        if num%i==0:
            lista=lista+[i]
    return len(lista)+1