def primo(num):
    """ Dado um número qualquer retorna a quantidade de divisores desse números;
    int-> int """
    i=0
    lista=[]
    if num<0:
        return 0
    for i in list(range(1,10)):
        if num%list(range(1,11))[i]==0:
            lista=lista+[list(range(1,11))[i]]
    i=i+1
    if num not in lista:
        lista=lista+[num]+[1]
    if len(lista)>2:
        return False
    else:
        return True