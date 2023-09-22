def qtd_divisores(num):
    """ Dado um número qualquer retorna a quantidade de divisores desse números;
    int-> int """
    i=1
    lista=[]
    if num<0:
        return 0
    for i in list(range(1,num)):
        if num%list(range(1,num+1))[i]==0:
            lista=lista+[list(range(1,num+1))[i]]
    i=i+1
    return len(lista)+1